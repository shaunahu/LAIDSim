from typing import TYPE_CHECKING
from Melodie import FloatParam, Visualizer

if TYPE_CHECKING:
    from source.model import LLMModel


class LLMVisualizer(Visualizer):
    model: "LLMModel"

    def setup(self):
        # Parameters to be controlled by users
        self.params_manager.add_param(
            FloatParam(
                name="seed_size",
                value_range=(0, 1),
                label="Seed Size (k)"))

        self.params_manager.add_param(
            FloatParam(
                name="influence_param",
                value_range=(0, 1),
                label="Influence Parameter (α)"))

        # Draw network
        self.add_network(name='influence_diffusion_network',
                         network_getter=lambda: self.model.network,
                         var_getter=lambda agent: agent.preference_state,
                         var_style={
                             0: {
                                 "label": "active",
                                 "color": "#00fb34"
                             },
                             1: {
                                 "label": "inactive",
                                 "color": "#fafb56"
                             }
                         })

        # Influence diffusion count line chart
        self.plot_charts.add_line_chart("Influence_diffusion_count_line").set_data_source({
            "active": lambda: self.model.environment.s0,
            "inactive": lambda: self.model.environment.s1,
            # "alteration_degree": lambda: self.model.environment.alteration_degree

        })

        # Influence diffusion count bar chart
        self.plot_charts.add_barchart("Influence_diffusion_count_bar").set_data_source({
            "active": lambda: self.model.environment.s0,
            "inactive": lambda: self.model.environment.s1
        })


