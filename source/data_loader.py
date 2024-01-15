from typing import TYPE_CHECKING, Dict, Any

import numpy as np

from Melodie import DataLoader
from source import data_info

if TYPE_CHECKING:
    from source.scenario import PreferenceComplexScenario

class PreferenceComplexDataLoader(DataLoader):
    def setup(self):
        self.load_dataframe(data_info.simulator_scenarios)
        self.load_dataframe(data_info.id_preference_state)
        self.generate_agent_dataframe()

    @staticmethod
    def init_preference_state(scenario: "PreferenceComplexScenario"):
        state = 0
        if np.random.uniform(0, 1) <= scenario.initial_infected_percentage:
            state = 1
        return state

    def generate_agent_dataframe(self):
        with self.dataframe_generator(
            data_info.agent_params, lambda scenario: scenario.agent_num
        ) as g:

            def generator_func(scenario: "PreferenceComplexScenario") -> Dict[str, Any]:
                return {
                    "id": g.increment(),
                    "preference_state": self.init_preference_state(scenario)
                }

            g.set_row_generator(generator_func)

