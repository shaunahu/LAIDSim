import numpy as np
from Melodie import Environment
from Melodie import AgentList
from source.agent import LLMSocialAgent
from source.scenario import LLMScenario
from source.tools import text2embedding

from sklearn.metrics.pairwise import cosine_similarity


class LLMEnvironment(Environment):
    scenario: "LLMScenario"

    def __init__(self):
        super().__init__()

    def setup(self):
        self.s0 = 0
        self.s1 = 0
        self.alteration_degree = 0

    @staticmethod
    def agents_infection(agents: "AgentList[LLMSocialAgent]"):
        for agent in agents:
            if agent.preference_state == 0:
                agent.infection(agents)

    def calc_population_infection_state(self, agents: "AgentList[LLMSocialAgent]"):
        self.setup()
        for agent in agents:
            if agent.preference_state == 0:
                self.s0 += 1
            elif agent.preference_state == 1:
                self.s1 += 1
        self.information_analysis(agents)

    def save_information_analysis(self, agents: "AgentList[LLMSocialAgent]"):
        filename = f"data/output/user_posts_{str(self.scenario.id)}.txt"
        with open(filename, 'w', encoding="utf-8") as file:
            for agent in agents:
                file.write("User ID " + str(agent.id + 1) + ": " + agent.post + "\n")

        filename = f"data/output/user_accepts_{str(self.scenario.id)}.txt"
        with open(filename, 'w', encoding="utf-8") as file:
            for agent in agents:
                if agent.influencer is not None:
                    prefix = "User ID " + str(agent.influencer.id+1) + " -> "
                else:
                    prefix = ""
                file.write(prefix + "User ID " + str(agent.id + 1) + ": " + agent.accept + "\n")

    def information_analysis(self, agents: "AgentList[LLMSocialAgent]"):
        active_users = []
        for agent in agents:
            if agent.influencer is not None:
                active_users.append(agent)

        alteration_degrees = []
        for au in active_users:
            m_k_altered = text2embedding(au.post)
            m_k = text2embedding(au.accept)

            alteration_degree = 1 - cosine_similarity(m_k.reshape(1, -1), m_k_altered.reshape(1, -1))
            alteration_degrees.append(alteration_degree)
        alteration_degrees = np.squeeze(np.array(alteration_degrees))
        self.alteration_degree = np.mean(alteration_degrees)
        print(self.alteration_degree)



