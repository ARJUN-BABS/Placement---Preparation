#Hackerrank link - https://www.hackerrank.com/challenges/max-array-sum/problem
def maxSubsetSum(arr):
    array = [[0 for i in range(2)] for j in range(len(arr) + 1)]
    for i in range(1,len(arr) + 1):
        sumEx = array[i-1][0]
        sumIn = array[i-1][1]
        array[i][0] = max(sumIn, sumEx)
        array[i][1] = sumEx + arr[i-1]
    print(array)
    return max(array[-1][0], array[-1][1], 0)
