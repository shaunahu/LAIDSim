import random
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

from typing import TYPE_CHECKING

from Melodie import NetworkAgent

if TYPE_CHECKING:
    from Melodie import AgentList


class PreferenceComplexAgent(NetworkAgent):
    scenario: "PreferenceComplexScenario"

    def set_category(self):
        self.category = 0

    def setup(self):
        self.preference_state: int = 0
        self.repository: list = []

    def infection(self, agents: "AgentList[PreferenceComplexAgent]"):
        neighbors = self.network.get_neighbors(self)

        PA_counter = 0
        NA_counter = 0
        IA_counter = 0
        for neighbor_category, neighbor_id in neighbors:
            neighbor_agent: "PreferenceComplexAgent" = agents.get_agent(neighbor_id)
            if neighbor_agent.preference_state == 1:
                PA_counter += 1
            elif neighbor_agent.preference_state == 2:
                NA_counter += 1
            else:
                IA_counter += 1
        # print(f'PA: {PA_counter} | NA: {NA_counter} | IA: {IA_counter}')

        for neighbor_category, neighbor_id in neighbors:
            neighbor_agent: "PreferenceComplexAgent" = agents.get_agent(neighbor_id)
            if neighbor_agent.preference_state != 0:
                # common preference similarity
                cps = cosine_similarity(self.repository.reshape(1, -1), neighbor_agent.repository.reshape(1, -1))
                # influence probability
                iip = cps * np.count_nonzero(self.repository) / np.count_nonzero(np.union1d(self.repository, neighbor_agent.repository))
                rand = np.random.rand()
                if rand < iip:
                    self.repository[-1] = neighbor_agent.repository[-1]
                    # state transition
                    rated = self.repository[self.repository != 0]
                    min_rating = np.min(rated)
                    max_rating = np.max(rated)
                    if min_rating == max_rating:
                        pcl = 0.5
                    else:
                        pcl = (self.repository[-1] - min_rating) / (max_rating - min_rating)

                    transit_prob_PA = 0.5 * pcl + 0.5 * (PA_counter / len(neighbors))
                    transit_prob_NA = 0.5 * (1-pcl) + 0.5 * (NA_counter / len(neighbors))
                    transit_prob_IA = 0.5 * (1-abs(pcl - 0.5)) + 0.5 * (IA_counter / len(neighbors))
                    rand = np.random.rand()

                    # print(f'PA: {transit_prob_PA} | NA: {transit_prob_NA} | IA: {transit_prob_IA}')
                    if rand < transit_prob_PA:
                        self.preference_state == 0
                    elif rand < transit_prob_IA + transit_prob_PA:
                        self.preference_state == 2
                    else:
                        self.preference_state = 1




