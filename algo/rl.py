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
        self.alpha = alpha # learning rate
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
        self.reward = None
        #while(not self.agent.world.isInTerminalState):
        for x in range (0,200):
            oldAgentPos = self.agent.agentPosition
            newAgentPos = None
            if self.policy.type == PolicyType.PRANDOM:
                self.logInfoBeforeAction()
                self.action = self.policy.pRandom()
                self.agent.move(self.action) # perform action
                newAgentPos = self.agent.agentPosition
                self.logInfoAfterAction()
                self.reward = self.agent.world.getCell(self.agent.agentPosition[0], self.agent.agentPosition[1]).reward # measure reward
                # Q(a,s)  (1-alpha)*Q(a,s) + alpha*[R(s’,a,s)+ γ*maxa’Q(a’,s’)]
                oldAgentPos.qValue = (1-self.alpha) * oldAgentPos.qValue + self.alpha * (self.reward + self.discount_factor * self.maxFutureReward(newAgentPos))# update q

    def maxFutureReward(self, newAgentPos):
        maxReward = 0
        for a in self.policy.applicableOperators:
            if self.agent.world.getCell(self.agent.getProjectedPos(newAgentPos, a)).reward > maxReward:
                maxReward = self.agent.world.getCell(self.agent.getProjectedPos(newAgentPos, a)).reward
        return maxReward

    def logInfoBeforeAction(self):
        print("Agent's position before move: ", end="")
        print(self.agent.agentPosition.__dict__)

    def logInfoAfterAction(self):
        print("Action Chosen at Random: ", end="")
        print(self.action.type.__dict__)
        print("Agent's position: ", end="")
        print(self.agent.agentPosition.__dict__)


    #def sarsa(self):

