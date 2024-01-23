from typing import TYPE_CHECKING

import numpy as np
import random

import Melodie
from Melodie import Model
from Melodie import Edge,Network

from source import data_info
from source.agent import LLMSocialAgent
from source.data_collector import LLMSocialNetworkDataCollector
from source.environment import LLMEnvironment
from source.scenario import LLMScenario
from source.tools import text2embedding, load_pickle

if TYPE_CHECKING:
    from Melodie import AgentList


class LLMModel(Model):
    scenario: "LLMScenario"

    def create(self):
        self.agents: "AgentList[LLMSocialAgent]" = self.create_agent_list(LLMSocialAgent)
        self.environment: LLMEnvironment = self.create_environment(LLMEnvironment)
        self.data_collector = self.create_data_collector(LLMSocialNetworkDataCollector)
        self.network = self.create_network()

    def setup(self):
        self.agents.setup_agents(
            agents_num=self.scenario.agent_num,
            params_df=self.scenario.get_dataframe(data_info.agent_params),
        )
        if self.scenario.get_network_params() != {}:
            self.network.setup_agent_connections(
                agent_lists=[self.agents],
                network_type=self.scenario.network_type,
                network_params=self.scenario.get_network_params(),
            )
        else:
            network = Network(model=LLMSocialAgent)
            self.network = network
            for agent in self.agents:
                self.network.add_agent(agent)
            # load network from file, make sure the filename is same with network_type in scenario.
            filename = f'data/input/{self.scenario.network_type}.txt'
            with open(filename, 'r') as file:
                for line in file:
                    u = int(line.strip().split()[0])
                    i = int(line.strip().split()[1])
                    edge = Edge(category_1=0, agent_1_id=u, category_2=0, agent_2_id=i, edge_properties={})
                    self.network.add_edge((0,u), (0,i), edge)

    def run(self):
        for period in self.iterator(self.scenario.period_num):
            if period == 0:
                self.initialisation()
            else:
                self.environment.agents_infection(self.agents)
            self.environment.calc_population_infection_state(self.agents)
            self.data_collector.collect(period)
        self.data_collector.save()
        self.environment.save_information_analysis(self.agents)

    def initialisation(self):
        user_profiles = []
        with open("data/input/user_profile.txt", "r") as file:
            for line in file.readlines():
                if line not in ['\n', '\r\n']:  # Check for the end of line
                    user_profile = line.split(": ")[1]
                    user_profiles.append(user_profile)

        user_embeddings = load_pickle('data/input/user_embedding.pickle')

        for index in range(len(self.agents)):
            agent = self.agents[index]
            agent.profile = user_profiles[index]
            agent.embedding = user_embeddings[index]
            index += 1

        seedSet = random.sample(list(self.agents), self.scenario.seed_size)
        for seed in seedSet:
            seed.preference_state = 1
            seed.post = self.scenario.influence_msg
            seed.accept = self.scenario.influence_msg
            seed.isSeed = True
            print(f'Seed user: {seed.id}')