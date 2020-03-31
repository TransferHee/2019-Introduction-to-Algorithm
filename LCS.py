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

x="ABCBKOLL"
y="BDCAFOLKO"
print("Longest Common Subsequence's length is : ",LCS(x,y))
