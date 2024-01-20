from Melodie import Environment
from Melodie import AgentList
from source.agent import LLMSocialAgent
from source.scenario import LLMScenario


class LLMEnvironment(Environment):
    scenario: "LLMScenario"

    def setup(self):
        self.s0 = 0
        self.s1 = 0

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

    def information_analysis(self, agents: "AgentList[LLMSocialAgent]"):
        filename = "data/output/user_posts.txt"
        with open(filename, 'w', encoding="utf-8") as file:
            for agent in agents:
                file.write("User ID " + str(agent.id + 1) + ": " + agent.post + "\n")

        filename = "data/output/user_accepts.txt"
        with open(filename, 'w', encoding="utf-8") as file:
            for agent in agents:
                file.write("User ID " + str(agent.id + 1) + ": " + agent.accept + "\n")


