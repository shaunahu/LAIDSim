from Melodie import Scenario

class LLMScenario(Scenario):
    def setup(self):
        self.period_num: int = 0
        self.agent_num: int = 0
        self.network_type: str = ""
        self.network_param_p: float = 0.0
        self.network_param_directed: str = ""
        self.initial_infected_pecentage: float = 0.0
        self.influence_msg: str = ""
        self.influence_param: float = 0.0
        self.seed_size: float = 0.0

    def get_network_params(self):
        if self.network_type == "erdos_renyi_graph":
            network_params = {"p": self.network_param_p, "directed": self.network_param_directed}
        elif self.network_type == "facebook":
            network_params = {}
        else:
            raise NotImplementedError
        return network_params
