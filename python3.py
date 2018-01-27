#!/usr/bin/python3

import sys
import random

permutation=[]
numJobs=0
numMachines=0
initData=[]

    
def init(filename):
    """
    Read data describing number of machines, jobs and processing times.
    """
    global initData
    global numJobs
    global numMachines

    file=open(filename,'r')
    d=file.read().split()
    numJobs=int(d[0])
    numMachines=int(d[1])
    poz=2
    for i in range(numMachines):
        cost=[]
        for j in range(numJobs):
            cost.append(int(d[poz]))
            poz+=1
        initData.append(cost)
    
    file.close()
    
def score(p):
    """
    Calculates the schedule length (the value that is minimized) for permutation p. 
    """
    global initData
    global numJobs
    global numMachines
    
    res = [0] * numMachines
    for i in range(numJobs):
        res[0] += initData[0][p[i]]
        for j in range(1, numMachines):
            res[j] = max(res[j], res[j-1]) + initData[j][p[i]]
    return res[-1]
    


def main(argv):
    global permutation

    init(argv[1])

if __name__ == "__main__":
    main(sys.argv)
    