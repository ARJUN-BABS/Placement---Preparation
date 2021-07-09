#Hackerrank - https://www.hackerrank.com/challenges/minimum-swaps-2/problem

def minimumSwaps(arr):
    swaps = 0
    index = 0
    while(index<len(arr)):
        if(index > arr[index] - 1):
            temp = arr[index]
            arr[index] = arr[arr[index] - 1]
            temp = arr[arr[index] - 1]
            swaps+=1
        else:
            index = index+1
    return swaps
            
