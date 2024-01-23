from Melodie import Simulator
from config import config
from source.data_loader import LLMDataLoader
from source.model import LLMModel
from source.scenario import LLMScenario
from source.visualizer import LLMVisualizer

if __name__ == "__main__":
    simulator = Simulator(
        config=config,
        model_cls=LLMModel,
        scenario_cls=LLMScenario,
        data_loader_cls=LLMDataLoader,
        visualizer_cls=LLMVisualizer
    )
    # simulator.run()
    simulator.run_visual()
