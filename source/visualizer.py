from typing import TYPE_CHECKING
from Melodie import FloatParam, Visualizer, StringParam
import os
import pandas as pd
# from MelodieInfra import StringParam

if TYPE_CHECKING:
    from source.model import LLMModel


class LLMVisualizer(Visualizer):
    model: "LLMModel"

    def setup(self):
        # Parameters to be controlled by users
        self.params_manager.add_param(
            FloatParam(
                name="seed_size",
                value_range=(1, self.get_agents_num()),  # make it dynamic; equal to the num of agents
                label=f"Seed Size (k) = [1 - {self.get_agents_num()}]"))

        self.params_manager.add_param(
            FloatParam(
                name="influence_param",
                value_range=(0, 1),
                label="Influence Parameter (α) = [0 - 1]"))

        # self.params_manager.add_param(
        #     FloatParam(
        #         name="id_scenario",
        #         label="Scenario ID [0 - 3]",
        #         value_range=(0, 3)
        #     )
        # )

        # Draw network
        self.add_network(name='influence_diffusion_network',
                         network_getter=lambda: self.model.network,
                         var_getter=lambda agent: agent.preference_state,
                         var_style={
                             0: {
                                 "label": "inactive",
                                 "color": "#fafb56"
                             },
                             1: {
                                 "label": "active",
                                 "color": "#00fb34"
                             }
                         })

        # Influence diffusion count line chart
        self.plot_charts.add_line_chart("Influence_diffusion_count_line").set_data_source({
            "inactive": lambda: self.model.environment.s0,
            "active": lambda: self.model.environment.s1,

        })

        self.plot_charts.add_line_chart("Average alteration_degree_line").set_data_source({
            "alteration_degree": lambda: self.model.environment.alteration_degree
        })

    @staticmethod
    def get_agents_num() -> int:
        data = pd.read_excel("data/input/SimulatorScenarios.xlsx", sheet_name="simulator_scenarios", engine="openpyxl")
        agents_num = data['agent_num'].max()
        return int(agents_num)