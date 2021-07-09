#Leetcode - https://leetcode.com/discuss/interview-question/356433/


#This is similar to the 0/1 knapsack dp but the difference is that we try to find the closest sum to a given value
def closestValueToValue(arr,s):
    dp = [[0 for i in range(s+1)] for j in range(len(arr) + 1)]
    for i in range(1,len(arr) + 1):
        for j in range(1,s+1):
            if(arr[i-1] <= j):
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-arr[i-1]] + arr[i-1])
            else:
                dp[i][j] = dp[i-1][j]
    return dp[-1][-1]
                
def minAbsDiff(arr):
    totalsum = sum(arr)
    x = closestValueToValue(arr,totalsum//2)
    return (totalsum - x) - x
    
