import numpy as np
import random

# Declare Variables
ROCK, PAPER, SCISSORS, NUM_ACTIONS = 0, 1, 2, 3 

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

# accmulate in stratSum
def getStrategy(regretSum):
    
    strategy = np.maximum(regretSum, 0)
    normalizingSum = np.sum(strategy)

    if normalizingSum > 0:
        strategy /= normalizingSum
    else:
        strategy = np.ones(NUM_ACTIONS)/NUM_ACTIONS
    
    return strategy

def getAction(strategy):
    # Returns a random number in (0,1)
    rr = random.random()
    # Returns 0, 1, 2 based on the mixed strategy
    return np.searchsorted(np.cumsum(strategy/np.sum(strategy)), rr)


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

def updateRegretSum(myStrat, oppStrat, regretSum, iter):
    # To train the algorithm and modify the regretSum array
    actionPayoff = np.zeros(NUM_ACTIONS)
    for i in range(iter):
        
        oppAction = getAction(oppStrat)       

       # Compute Action Payoffs: ROCK 0; PAPER 1; SCISSORS 2
        actionPayoff[oppAction] = 0 
        actionPayoff[(oppAction+1)%NUM_ACTIONS] = 1
        actionPayoff[(oppAction+2)%NUM_ACTIONS] = -1 

        regretSum += actionPayoff

    return regretSum

def main():
    # Opponent uses the mixed strat (R, S, P) = (0.4, 0.3, 0.3)
    oppDefStrategy = np.array([0.4, 0.3, 0.3])
    strategy = np.zeros(NUM_ACTIONS)
    regretSum = np.zeros(NUM_ACTIONS)
    
    myStrat = getStrategy(regretSum) # Use default mixed strat (1/3, 1/3, 1/3)

    print("Using default mixed strategy (1/3, 1/3, 1/3)")
    print(getStrategyPayoff(myStrat, oppDefStrategy, 100, 100))

    regretSum =  updateRegretSum(myStrat, oppDefStrategy, regretSum ,100000) # Modify global variable regretSum
    myNewStrat = getStrategy(regretSum)

    print("Using Regret matched mixed strategy after training: ", myNewStrat)
    print(getStrategyPayoff(myNewStrat, oppDefStrategy, 100, 100))

main()