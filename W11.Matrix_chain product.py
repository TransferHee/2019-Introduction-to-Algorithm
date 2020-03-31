S = [5, 2, 3, 4, 6] 

def matrix_chain(S):
    size = len(S) - 1
    
    # Step 1. initialize for memoization
    cache = [[0] * size for _ in range(size)]
    for i in range(size):
        cache[i][i] = 0

    # Step 2. calculate the minimum number of operations
    for b in range(1, size):
        # b = j - i is the length of the problem, 
        for i in range(0, size - b):
            j = b + i
            cache[i][j] = float('inf')
            for k in range(i, j):
                cache[i][j] = min(cache[i][j], cache[i][k] + cache[k+1][j] + (S[i] * S[k+1] * S[j+1]))
    for i in range(len(cache)):
        print(cache[i])
    return cache[0][size-1]           

print("The minimum number of operations =", matrix_chain(S))

def matrix_chain2(S):
    size = len(S)-1

    cache=[[0]*size for _ in range(size)]

    for i in range(size):
        cache[i][i]=0

    for b in range(1,size):
        for i in range(size-b):
            j=b+i
            cache[i][j] = float('inf')
            for k in range(i,j):
                cache[i][j] = min(cache[i][j], cache[i][k] + cache[k+1][j] +(S[i] *S[k+1] * S[j+1]))
    for i in range(len(cache)):
        print(cache[i])
    return cache[0][size-1]


print("The minimum number of operations =", matrix_chain2(S))


def mc(s):
    size = len(s)-1

    x=[[0] * size for q in range(size)]

    for b in range(1,size):
        for i in range(size-b):
            j=b+i
            x[i][j]=float('inf')
            for k in range(i,j):
                x[i][j]=min(x[i][j], x[i][k]+x[k+1][j] + (s[i]*s[k+1]*s[j+1]))
    return x[0][size-1]




def ms(s):
    size = len(s)-1
    x=[[0]*size for _ in range(size)]

    for b in range(1,size):
        for i in range(size-b):
            j=b+i
            x[i][j]=float('inf')
            for k in range(i,j):
                x[i][j]=min(x[i][j], x[i][k] + x[k+1][j] + (s[i] * s[k+1] * s[j+1]))
    return x[0][size-1]




