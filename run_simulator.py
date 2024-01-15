from Melodie import Simulator
from config import config
from source.data_loader import PreferenceComplexDataLoader
from source.model import PreferenceModel
from source.scenario import PreferenceComplexScenario

if __name__ == "__main__":
    simulator = Simulator(
        config=config,
        model_cls=PreferenceModel,
        scenario_cls=PreferenceComplexScenario,
        data_loader_cls=PreferenceComplexDataLoader
    )
    simulator.run()
