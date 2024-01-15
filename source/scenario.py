from Melodie import Scenario

class PreferenceComplexScenario(Scenario):
    def setup(self):
        self.period_num: int = 0
        self.agent_num: int = 0
        self.network_type: str = ""
        self.network_param_p: float = 0.0
        self.network_param_directed: str = ""
        self.initial_infected_percentage: float = 0.0
        self.infection_prob: float = 0.0
        self.item_num: int = 0

    def get_network_params(self):
        if self.network_type == "erdos_renyi_graph":
            network_params = {"p": self.network_param_p, "directed": self.network_param_directed}
        elif self.network_type == "facebook":
            network_params = {}
        else:
            raise NotImplementedError
        return network_params
