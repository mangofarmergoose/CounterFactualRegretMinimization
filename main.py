import numpy as np
import random

NUM_ACTIONS = 3
ROCK, PAPER, SCISSORS = 0, 1, 2

# Returns the adjusted strategy after an iteration
def getStrategy(regretSum,strategySum):
    normalizingSum = 0
    strategy = [0,0,0]
    #Normalizingsum is the sum of positive regrets. 
    #This ensures do not 'over-adjust' and converge to equilibrium
    for i in range(NUM_ACTIONS):
        if regretSum[i] > 0:
            strategy[i] = regretSum[i]
        else:
            strategy[i] = 0
        normalizingSum += strategy[i]
    ##This loop normalizes our updated strategy
    for i in range(NUM_ACTIONS):
        if normalizingSum > 0:
            strategy[i] /= normalizingSum
        else:
            #Default to 33%
            strategy[i] = 1.0 / NUM_ACTIONS
        strategySum[i] += strategy[i]
    return (strategy,strategySum)        

def getAction(strategy):
    # Returns a random number in (0,1)
    rr = random.random()
    # Returns 0, 1, 2 based on the mixed strategy
    return np.searchsorted(np.cumsum(strategy/np.sum(strategy)), rr)

def train(iters, regretSum, oppStrategy):
    actionUtility = np.zeros(NUM_ACTIONS)
    strategySum = np.zeros(NUM_ACTIONS)
    
    for i in range(0,iters):
        # Retrieve Actions
        t = getStrategy(regretSum,strategySum)
        strategy = t[0]
        strategySum = t[1]
        myAction = getAction(strategy)
        # Define an arbitrary opponent strategy from which to adjust
        oppAction = getAction(oppStrategy)   
        # Opponent Chooses scissors
        if oppAction == SCISSORS:
            actionUtility[ROCK] = 1
            actionUtility[PAPER] = -1
        # Opponent Chooses Rock
        elif oppAction == ROCK:
            actionUtility[SCISSORS] = -1
            actionUtility[PAPER] = 1
        # Opopnent Chooses Paper
        else:
            actionUtility[ROCK] = -1
            actionUtility[SCISSORS] = 1
            
        # Add the regrets from this decision
        for i in range(NUM_ACTIONS):
            regretSum[i] += actionUtility[i] - actionUtility[myAction]
            
    return strategySum

def getAverageStrategy(iters, oppStrat):
    strategySum = train(iters,np.zeros(NUM_ACTIONS),oppStrat)
    avgStrategy = np.zeros(NUM_ACTIONS)
    normalizingSum = 0
    for i in range(NUM_ACTIONS):
        normalizingSum += strategySum[i]
    for i in range(NUM_ACTIONS):
        if normalizingSum > 0:
            avgStrategy[i] = strategySum[i] / normalizingSum
        else:
            avgStrategy[i] = 1.0 / NUM_ACTIONS
    return avgStrategy

def getValue(p1, p2):
    if p1 == p2:
        return 0 
    if p1 == ROCK and p2 == SCISSORS:
        return 1
    if p1 == SCISSORS and p2 == PAPER:
        return 1
    if p1 == PAPER and p2 == ROCK:
        return 1
    else:
        return -1
    
def getStrategyPayoff(myStrat, oppStrat, iter1, iter2):
    vvv = []
    for i in range(iter1):
        vv = 0 
        for j in range(iter2):
            myAction = getAction(myStrat)
            oppAction = getAction(oppStrat)
            vv += getValue(myAction, oppAction)
        vvv.append(vv)

    return np.mean(vvv)
    
oppStrat = [0.4,0.3,0.3]
myNewStrat = getAverageStrategy(100000, oppStrat)
print("Opponent's Strategy: ",oppStrat)
print("Maximally Exploitative Strat: ", myNewStrat)
print("Our Payoff: ", getStrategyPayoff(myNewStrat, oppStrat, 100, 100))

#Two player training Function
def train2Player(iterations,regretSum1,regretSum2,p2Strat):
    ##Adapt Train Function for two players
    actionUtility = [0,0,0]
    strategySum1 = [0,0,0]
    strategySum2 = [0,0,0]
    for i in range(0,iterations):
        ##Retrieve Actions
        t1 = getStrategy(regretSum1,strategySum1)
        strategy1 = t1[0]
        strategySum1 = t1[1]
        myAction = getAction(strategy1)
        
        t2 = getStrategy(regretSum2,p2Strat)
        strategy2 = t2[0]
        strategySum2 = t2[1]
        oppAction = getAction(strategy2)
        
        # Opponent Chooses scissors
        if oppAction == SCISSORS:
            actionUtility[ROCK] = 1
            actionUtility[PAPER] = -1
        # Opponent Chooses Rock
        elif oppAction == ROCK:
            actionUtility[SCISSORS] = -1
            actionUtility[PAPER] = 1
        # Opopnent Chooses Paper
        else:
            actionUtility[ROCK] = -1
            actionUtility[SCISSORS] = 1
            
        # Add the regrets from this decision
        for i in range(NUM_ACTIONS):
            regretSum1[i] += actionUtility[i] - actionUtility[myAction]
            regretSum2[i] += -(actionUtility[i] - actionUtility[myAction])
    return (strategySum1, strategySum2)

# Returns the Mixed Nash Equilibrium reached by two opponents through Regret Matching
def convergeToNash(iters,oppStrat):
    strats = train2Player(iters,[0,0,0],[0,0,0],oppStrat)
    s1 = np.sum(strats[0])
    s2 = np.sum(strats[1])
    for i in range(NUM_ACTIONS):
        if s1 > 0:
            strats[0][i] = strats[0][i]/s1
        if s2 > 0:
            strats[1][i] = strats[1][i]/s2
    return strats

nashEq = convergeToNash(100000, [0.4,0.3,0.3])
payoffP1 = getStrategyPayoff(nashEq[0], nashEq[1], 100, 100)

print("Mixed Strategy used by Player 1:", nashEq[0])
print("Mixed Strategy used by Player 2:", nashEq[1])
print("Payoff of Player 1: ", payoffP1)
print("Payoff of Player 2 ", -payoffP1)
