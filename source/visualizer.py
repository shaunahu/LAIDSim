from typing import TYPE_CHECKING
from Melodie import FloatParam, Visualizer

if TYPE_CHECKING:
    from source.model import PreferenceModel


class PreferenceVisualizer(Visualizer):
    model: "PreferenceModel"

    def setup(self):
        self.params_manager.add_param(FloatParam(
            name='infection_prob',
            value_range=(0, 1),
            label="Influence Diffusion Probability (%)"
        ))

        self.add_network(name='influence_diffusion_network',
                         network_getter=lambda: self.model.network,
                         var_getter=lambda agent: agent.preference_state,
                         var_style={
                             0: {
                                 "label": "IA",
                                 "color": "#00fb34"
                             },
                             1: {
                                 "label": "PA",
                                 "color": "#fafb56"
                             },
                             2: {
                                 "label": "NA",
                                 "color": "#3434b8"
                             }
                         })

        self.plot_charts.add_line_chart("Influence_diffusion_count_line").set_data_source({
            "IA": lambda: self.model.environment.s0,
            "PA": lambda: self.model.environment.s1,
            "NA": lambda: self.model.environment.s2
        })

        # self.plot_charts.add_barchart("Influence_diffusion_count_bar").set_data_source({
        #     "IA": lambda: self.model.environment.s0,
        #     "PA": lambda: self.model.environment.s1,
        #     "NA": lambda: self.model.environment.s2
        # })

        # self.plot_charts.add_piechart("Influence_diffusion_count_bar").set_data_source({
        #     "IA": lambda: self.model.environment.s0,
        #     "PA": lambda: self.model.environment.s1,
        #     "NA": lambda: self.model.environment.s2
        # })


