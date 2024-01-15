from typing import TYPE_CHECKING

import numpy as np
import random

import Melodie
from Melodie import Model
from Melodie import Edge,Network

from source import data_info
from source.agent import PreferenceComplexAgent
from source.data_collector import PreferenceComplexDataCollector
from source.environment import PreferenceComplexEnvironment
from source.scenario import PreferenceComplexScenario

if TYPE_CHECKING:
    from Melodie import AgentList


class PreferenceModel(Model):
    scenario: "PreferenceComplexScenario"

    def create(self):
        self.agents: "AgentList[PreferenceComplexAgent]" = self.create_agent_list(PreferenceComplexAgent)
        self.environment: PreferenceComplexEnvironment = self.create_environment(PreferenceComplexEnvironment)
        self.data_collector = self.create_data_collector(PreferenceComplexDataCollector)
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
            network = Network(model=PreferenceComplexAgent)
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
            self.environment.agents_infection(self.agents)
            # self.environment.agents_state_transition(self.agents)
            self.environment.calc_population_infection_state(self.agents)
            self.data_collector.collect(period)
        self.data_collector.save()

    def initialisation(self):
        for agent in self.agents:
            agent.repository = [random.randint(0, 5) for _ in range(self.scenario.item_num)]
            if agent.preference_state == 1:
                rating = random.randint(1, 5)
                agent.repository.append(rating)
            else:
                agent.repository.append(0)
            agent.repository = np.array(agent.repository)
            # set initial state
            if agent.preference_state == 1:
                rated = agent.repository[agent.repository != 0]
                min_rating = np.min(rated)
                max_rating = np.max(rated)
                if min_rating == max_rating:
                    agent.preference_state == 0
                else:
                    pcl = (agent.repository[-1] - min_rating) / (max_rating - min_rating)
                    if pcl > 0.5:
                        agent.preference_state = 1
                    else:
                        agent.preference_state = 2
