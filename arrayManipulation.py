# Hackerrank - https://www.hackerrank.com/challenges/crush/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

def arrayManipulation(n, queries):
    # Write your code here
    arr = [0 for i in range(n)]
    for query in queries:
        arr[query[0] - 1] += query[2]
        if(query[1] < n):
            arr[query[1]] += (-query[2])
    
    maxsum = 0
    tempsum = 0
    for el in arr:
        tempsum+=el
        if(tempsum>maxsum):
            maxsum = tempsum
    return maxsum
