"""" PEPLOIT: If pickup and dropoff is applicable, 
    choose this operator; 
    otherwise, apply the applicable operator with the highest q-value 
    (break ties by rolling a dice for operators with the same q-value) 
    with probability 0.8 and choose a different applicable operator randomly with probability 0.2. """
import random

class Policy:
    applicableOperators = []
    canPickup = True
    canDropoff = True
    world = None
    agent = None
    def __init__(self, world, agent):
        self.world = world
        self.agent = agent
        for o in self.agent.operators:
            if o.getApplicability() is True:
                self.applicableOperators.append(o)


    def pRandom(self, operator):
        if(self.canDropoff and self.canPickup):
            return operator
        else:
            randomOperator = random.randint(0,self.applicableOperators.__len__())
            if self.applicableOperators is not None:
                return self.applicableOperators[randomOperator]

    # def pExploit(self, operator):
    #
    # def pGreedy(self, operator):

