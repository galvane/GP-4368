# reinforcement learning
from numpy.core._dtype import __repr__

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
        self.position = self.agent.agentPosition #initial state
        action = None
        #while(not self.agent.world.isInTerminalState):
        for x in range (0,2):
            if self.policy.type == PolicyType.PRANDOM:
                print("Agent's position before move: ", end="")
                print(self.agent.agentPosition.__dict__)
                self.action = self.policy.pRandom()
                self.agent.move(self.action)
                print ("Action Chosen at Random: ",end="")
                print(self.action.type.__dict__)
                print("Agent's position: ", end="")
                print(self.agent.agentPosition.__dict__)


    #def sarsa(self):

