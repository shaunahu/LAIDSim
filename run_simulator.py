from Melodie import Simulator
from config import config
from source.data_loader import PreferenceComplexDataLoader
from source.model import PreferenceModel
from source.scenario import PreferenceComplexScenario
from source.visualizer import PreferenceVisualizer

if __name__ == "__main__":
    simulator = Simulator(
        config=config,
        model_cls=PreferenceModel,
        scenario_cls=PreferenceComplexScenario,
        data_loader_cls=PreferenceComplexDataLoader,
        visualizer_cls=PreferenceVisualizer
    )
    # simulator.run()
    simulator.run_visual()