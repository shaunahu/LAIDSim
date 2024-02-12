import random
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import torch

from typing import TYPE_CHECKING

from Melodie import NetworkAgent
from source.tools import text2embedding
from source.LLM_module import generate_information

if TYPE_CHECKING:
    from Melodie import AgentList


class LLMSocialAgent(NetworkAgent):
    scenario: "LLMScenario"

    def set_category(self):
        self.category = 0

    def setup(self):
        self.preference_state: int = 0
        self.profile: str = ""
        self.post: str = ""
        self.accept: str = ""
        self.embedding: np.ndarray = None
        self.isSeed: bool = False
        self.influencer: LLMSocialAgent = None

    def infection(self, agents: "AgentList[LLMSocialAgent]"):
        try:
            neighbors = self.network.get_neighbors(self)

            for neighbor_category, neighbor_id in neighbors:
                neighbor_agent: "LLMSocialAgent" = agents.get_agent(neighbor_id)
                if neighbor_agent.preference_state == 1:
                    rand = np.random.rand()
                    influence_prob = self.calculate_influence_prob(neighbor_agent)
                    if rand < influence_prob:
                        self.preference_state = neighbor_agent.preference_state
                        self.accept = neighbor_agent.post
                        if not self.isSeed:
                            self.post = generate_information(self.accept, self.profile)
                            print(f"Agent ID: {self.id}, Agent post: {self.post} ")
                            self.influencer = neighbor_agent
                            # self.post = neighbor_agent.post
        except Exception as e:
            self.preference_state = 0


    def calculate_influence_prob(self, neighbor_agent):
        ki = self.embedding
        kj = neighbor_agent.embedding
        cx = text2embedding(neighbor_agent.post)

        social_influence = cosine_similarity(kj.reshape(1, -1), ki.reshape(1, -1))
        content_influence = cosine_similarity(cx.reshape(1, -1), ki.reshape(1, -1))
        influence_prob = (self.scenario.influence_param * social_influence
                          + (1-self.scenario.influence_param) * content_influence)
        return influence_prob






