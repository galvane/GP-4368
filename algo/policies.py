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

    def pExploit(self, operator):
        if (self.canDropoff and self.canPickup):
            return operator
        else:
            highestQValue = 0
            op = None
            randomOperator = random.randint(0, self.applicableOperators.__len__())
            for o in self.applicableOperators:
                if o.qValue > highestQValue:
                    highestQValue = o.qValue
                    probability = [highestQValue]*80 * self.applicableOperators[randomOperator] * 20
                    random.choice(probability)
                    op = o
                elif o.qValue == highestQValue:
                    highestQValue = self.break_tie(o.qValue, highestQValue)
                    op = o
            return op

    def pGreedy(self, operator):
        if (self.canDropoff and self.canPickup):
            return operator
        else:
            highestQValue = 0
            op = None
            for o in self.applicableOperators:
                if o.qValue > highestQValue:
                    highestQValue = o.qValue
                    op = o
                elif o.qValue == highestQValue:
                    highestQValue = self.break_tie(o.qValue, highestQValue)
                    op = o
            return op

    def break_tie(self, o1, o2):
        randomOp = random.randint(0,2)
        if randomOp == 1:
            return o1
        return o2


