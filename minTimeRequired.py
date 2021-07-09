#Hackerrank - https://www.hackerrank.com/challenges/minimum-time-required/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=search

def findWork(arr,time):
    total = 0
    for el in arr:
        total+=(time//el)
    return total

# Complete the minTime function below.
def minTime(machines, goal):
    low = 1
    high = max(machines)*goal
    #print(high)
    #exit(0)
    currentmin = high
    while(low<high):
        mid = (low+high)//2
        workdone = findWork(machines,mid)
        if(workdone<goal):
            low = mid+1
        else:
            currentmin = mid
            high = mid
            
    return currentmin
