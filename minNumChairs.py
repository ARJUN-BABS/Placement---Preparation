#Leetcode - https://leetcode.com/discuss/interview-question/356520

def minNumChairs(S,K):
    i=0
    j=0
    count = 0
    maxcount = 0
    while(i<len(S)):
        if(S[i]<=K[j]):
            count+=1
            maxcount = max(count,maxcount)
            i+=1
        else:
            j+=1
            count-=1
    return maxcount
