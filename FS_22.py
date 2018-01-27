#!/usr/bin/python3

import sys
import random

numJobs = 0
numMachines = 0
initData = []
S = []
AN =[]
Ins = []


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

    for j in Ins:
        perw = 0
        for i in range(numMachines):
                AN[i] += (perw+initData[i][j])
                perw = AN[i]
    ans = ""
    for i in Ins:
        ans += str(i) + " "
    ans = ans[:-1]
    print(ans)


if __name__ == "__main__":
    main(sys.argv)
