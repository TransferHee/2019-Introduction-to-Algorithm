import sys
input = sys.stdin.readline

def Stair(l,stair):
    if l==1:
        return stair[0]
    elif l==2:
        return stair[0]+stair[1]
    elif l==3:
        return stair[2] + max(stair[0], stair[1])
    x=[]
    x.append(stair[0])
    x.append(stair[0] + stair[1])
    x.append(max(stair[0]+stair[2], stair[1] + stair[2]))
    for i in range(3,l):
        x.append(stair[i] + max(stair[i-1] + x[i-3], x[i-2]))
    print(x)
    return x[l-1]
def main():
    l=int(input())
    stair=[]
    for i in range(l):
        stair.append(int(input()))
    print(Stair(l,stair))
main()
