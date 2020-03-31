def minCost(cost, m, n):
    x = [[0 for x in range(m+1)] for x in range(n+1)] 
    
    x[0][0] = cost[0][0]
    
    for i in range(1, m+1): 
        x[i][0] = x[i-1][0] + cost[i][0] 
    for j in range(1, n+1): 
        x[0][j] = x[0][j-1] + cost[0][j]
    for i in range(1, m+1): 
        for j in range(1, n+1): 
            x[i][j] = min(x[i-1][j], x[i][j-1]) + cost[i][j]

    for i in range(len(x)):
        print(x[i])
    return x[m][n]

cost = [[1, 2, 3], 
        [4, 8, 2], 
        [1, 5, 3]]

print(minCost(cost, 2, 2))
print()
def fib2(n):
    v = [0,1]
    for i in range(2,n+1):
        v.append(v[i-1]+v[i-2])
    return v[n]

for i in range(10):
    print(fib2(i),end=' ')
print()
print()
def bin(n,r):
    v=[[0]*(n+1) for _ in range(n+1)]
    for i in range(n+1):
        for j in range(i):
            if(j==0 or i==j):
                v[i][j]=1
            else:
                v[i][j]=v[i-1][j-1]+v[i-1][j]
        print(v[i])
    return v[n][r]+v[n][r-1]
print(bin(5,3))
print()
print()

def LCS(x,y):
    
    #init
    m=len(x)
    n=len(y)
    c=[[0] * (n+1) for q in range(m+1)]
    
    #calculate
    for i in range(1,m+1):
        for j in range(1,n+1):
            if x[i-1]==y[j-1]:
                c[i][j]=c[i-1][j-1]+1
            else:
                c[i][j]=max(c[i-1][j], c[i][j-1])
    
    #show
    print("   y  ",end='')
    for j in range(n):
        print(y[j], end='  ')
    print()
    for k in range(len(c)):
        if(k==0):
            print("x",c[k])
        else:
            print(x[k-1],c[k])
    return c[m][n]

x="providence"
y="president"
print("Longest Common Subsequence's length is : ",LCS(x,y))


def shell_sort(arr):
    h=len(arr)//2
    while h >0:
        for i in range(h,len(arr)):
            j=i
            while j >= h and arr[j] < arr[j-h]:
                arr[j], arr[j-h] = arr[j-h], arr[j]
                j-=h
        h//=2

    return arr
