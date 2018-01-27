#!/usr/bin/python3

import sys
import random

numJobs = 0
numMachines = 0
initData = []
S = []
AN =[]
Ins = []
P = []
A = []
B = []


def score(p):
    """
    Calculates the schedule length (the value that is minimized) for permutation p.
    """
    global initData
    global numJobs
    global numMachines

    res = [0] * numMachines
    for i in range(len(p)):
        res[0] += initData[0][p[i]]
        for j in range(1, numMachines):
            res[j] = max(res[j], res[j - 1]) + initData[j][p[i]]
    return res[-1]

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


def main(argv):
    global initData
    global numJobs
    global numMachines
    global S
    global AN
    global Ins
    global P
    global A
    global B


    init(argv[1])
    for i in range(numJobs):
        S.append([0,i])
    for i in range(numMachines):
        for j in range(numJobs):
            S[j][0] += initData[i][j]
    AN = [0]*(numMachines)
    S= sorted(S)

    for i in S:
        Ins.append(i[1])
    for i in Ins:
        A.append(i)
        B.insert(0,i)
        if score(A) < score(B):
            P = A
        else:
            P = B
    ans = ""
    for i in P:
        ans += str(i) + " "
    ans = ans[:-1]
    print(ans)
#    print(score(P))



if __name__ == "__main__":
    main(sys.argv)
