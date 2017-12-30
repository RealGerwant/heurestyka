import fileinput
A=[]
for line in fileinput.input():
    A.append(line.split())
for i in A:
    print(i[0])