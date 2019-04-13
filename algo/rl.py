# reinforcement learning
from algo.policies import PolicyType


class RL:
    alpha = None
    discount_factor = None
    steps = 0
    steps2 = 0 #for experiments that switch policies
    policy = None
    policy2 = None

    def __init__(self, alpha, dF):
        self.alpha
        self.discount_factor = dF

    def qLearning(self, steps, policy, steps2, policy2):
        self.steps = steps
        self.policy = policy
        if steps2 is not None:
            self.steps2 = steps2
        if policy2 is not None:
            self.policy2 = policy2

    def SARSA(self, steps, policy, steps2, policy2):
        self.steps = steps
        self.policy = policy
        if steps2 is not None:
            self.steps2 = steps2
        if policy2 is not None:
            self.policy2 = policy2

