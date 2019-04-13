from algo.policies import PolicyType
from algo.rl import RL


class Experiment:

    def experiment1(self):
        rl = RL(0.3, 0.5)
        rl.qLearning(4000, PolicyType.PRANDOM)
        rl.qLearning(4000, PolicyType.PGREEDY)

    def experiment2(self):
        rl = RL(0.3, 0.5)
        rl.qLearning(200, PolicyType.PRANDOM, 7800, PolicyType.PEXPLOIT, )

    def experiment3(self):
        rl = RL(0.3, 0.5)
        rl.SARSA(200, PolicyType.PRANDOM, 7800, PolicyType.PEXPLOIT)

    def experiment4(self):
        rl = RL(0.3, 1.0)
        rl.SARSA(200, PolicyType.PRANDOM, 7800, PolicyType.PEXPLOIT)

    def experiment5(self):
        rl = RL(0.3, 0.5)
        rl.qLearning(200, PolicyType.PRANDOM, 7800, PolicyType.PEXPLOIT)
        # after the agent reaches a terminal state the second time, you will swap pickup and drop-off locations
