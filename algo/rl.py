# reinforcement learning
from algo.policies import PolicyType

class RL:
    alpha = None
    discount_factor = None
    steps = 0
    steps2 = 0  # for experiments that switch policies
    policy = None
    policy2 = None
    agent = None

    def __init__(self, alpha, dF, steps, policy, steps2, policy2):
        self.alpha = alpha
        self.discount_factor = dF
        self.steps = steps
        self.policy = policy
        self.steps2 = steps2
        self.policy2 = policy2

    def setAgent(self, agent):
        self.agent = agent

    def qLearn(self):
        self.position = self.agent.position #initial state
        while(not self.agent.world.isInTerminalState):

    def sarsa(self):

