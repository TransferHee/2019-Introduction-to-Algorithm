def knapsack(wv_list, max_weight):
    dp = [0] * (max_weight+1)
    for w, v in wv_list:
        for i in range(max_weight, 0, -1):
            if i-w < 0:
                continue
            if i-w > 0 and dp[i-w] == 0:
                continue
            print('dp[i-w]:{}, v:{} at {}'.format(dp[i-w], v, i))
            dp[i] = max(dp[i], dp[i-w]+v)
    print(dp)
    return dp[max_weight]

if __name__ == '__main__':
    # w, v
    arr = [(2,3), (1,2), (3,4), (2,2)]
    print(knapsack(arr, 5))
    print()
    print()

def knapsack1(capacity, n):
    array = [[0 for _ in range(capacity+2)] for _ in range(n+2)]
    for i in range(1, n+1):
        for s in range(1, capacity+1):
            if size[i-1] > s: # 물건의 부피가 s보다 크면
                array[i][s] = array[i - 1][s]
            else: # 물건의 부피가 s보다 작거나 같으면
                array[i][s] = max(value[i-1] + array[i-1][s-size[i-1]], array[i-1][s])
            print('%2d' % array[i][s], end=' ')
        print()
    return array[n][capacity]
size = [9, 3, 4, 7, 8]
value = [13, 4, 5, 10, 11]
print(knapsack1(10, 5))
