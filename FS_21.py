#!/usr/bin/python3

import sys
import random

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
    for line in file:
        initData.append(line.split())
    file.close()
    numJobs = int(initData[0][0])
    numMachines = int(initData[0][1])
    del initData[0]
    for i in range(len(initData)):
        for j in range(len(initData[0])):
            initData [i][j] = int(initData[i][j])

def main(argv):
    global initData
    global numJobs
    global numMachines

    init(argv[1])
    ans = ""
    for i in range(numJobs):
        ans += str(i) + " "
    ans = ans[:-1]
    print(ans)

if __name__ == "__main__":
    main(sys.argv)
    