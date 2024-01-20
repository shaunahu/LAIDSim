from Melodie import DataCollector


class LLMSocialNetworkDataCollector(DataCollector):
    def setup(self):
        self.add_agent_property("agents", "preference_state")
        self.add_environment_property("s0")
        self.add_environment_property("s1")
