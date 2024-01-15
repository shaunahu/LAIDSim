from config import config
from source.analyzer import PreferenceAnalyzer

if __name__ == "__main__":

    analyzer = PreferenceAnalyzer(config)
    analyzer.plot_health_state_share(id_scenario=0)
