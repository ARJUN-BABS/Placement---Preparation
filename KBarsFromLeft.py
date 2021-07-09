# Gfg - https://www.geeksforgeeks.org/?p=598292
def fact(n):
    val = 1
    for i in range(2,n+1):
        val*=i
    return val
  
  def iterative(N,K):
    dp = [[0 for i in range(K+1)] for j in range(N+1)]
    dp[0][0] =0
    for i in range(1,N+1) : 
        dp[i][1] = fact(i-1)
    for i in range(1, N+1):
        for j in range(2,K+1):
            if(j>i):
                dp[i][j] = 0
            else:
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j]*(i-1)
    return dp[-1][-1]
