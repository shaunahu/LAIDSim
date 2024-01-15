from Melodie import Environment
from Melodie import AgentList
from source.agent import PreferenceComplexAgent
from source.scenario import PreferenceComplexScenario


class PreferenceComplexEnvironment(Environment):
    scenario: "PreferenceComplexScenario"

    def setup(self):
        self.s0 = 0
        self.s1 = 0
        self.s2 = 0

    @staticmethod
    def agents_infection(agents: "AgentList[PreferenceComplexAgent]"):
        for agent in agents:
            agent.infection(agents)

    def calc_population_infection_state(self, agents: "AgentList[PreferenceComplexAgent]"):
        self.setup()
        for agent in agents:
            if agent.preference_state == 0:
                self.s0 += 1
            elif agent.preference_state == 1:
                self.s1 += 1
            elif agent.preference_state == 2:
                self.s2 += 1
