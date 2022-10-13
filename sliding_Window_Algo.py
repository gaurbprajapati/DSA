# Q1 Max Sum Subarray of size K

class Solution:
    def maximumSumSubarray (self,K,Arr,N):
        i=0
        j=0
        s=0
        ans=0

        while (j<len(Arr)):
            s+=Arr[j]
            if (j-i+1)<K:
                j+=1
            else:
                if (j-i+1)==K:
                    ans=max(ans,s)
                    s-=Arr[i]
                    i+=1
                    j+=1
        return ans


#Q2 First negative integer in every window of size k




def printFirstNegativeInteger( A, N, K):
    i=0
    j=0
    q=[]
    an=[]
    while (j<N):
        if (A[j]<0):
            q.append(A[j])
        if (j-i+1)<K:
            j+=1
        else:
            if (j-i+1)==K:
                if len(q)==0:
                    an.append(0)
                else:
                    an.append(q[0])
                    if (A[i]==q[0]):
                        q.pop(0)
                i+=1
                j+=1
    return an
print(printFirstNegativeInteger([-8,2,3,-6,10],5,2))


# --------------- question 3 Count Occurences of Anagrams 

# Count Occurences of Anagrams 
from  collections import Counter

def fun(s):
    d={}
    for i in s:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    return d

def search (pat ,txt):
    k=len(pat)
    ma=fun(pat)
    i=0
    j=0
    count=len(ma)
    ans=0
    while (j<len(txt)):
        #calculation
        if txt[j] in ma:
            if ma[txt[j]]>0:
                ma[txt[j]]-=1
        # if txt[j] in ma:
        if txt[j] in ma:
            if ma[txt[j]]==0:
                count-=1

        if (j-i+1)<k:
            j+=1
        else:
            if (j-i+1)==k:
                if (count==0):
                    ans+=1
                if txt[i] in ma:
                    ma[txt[i]]+=1
                    if ma[txt[i]]==0:
                        count-=1

                i+=1
                j+=1
    return ans
# txt = "forxxorfxdofr"
# pat = "for" 
# txt="kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk"
# pat="kkkkk"

txt="usjgmhcmhgdnmphnqkamhurktrffaclvgrzkkldacl"
pat="lteojomonxrqyjzginrnnzwacxxaedrwudxzrfu"
s = "cbaebabacd"
p = "abc"
# print(search(p,s))         
print(search(pat,txt)) 
# print(Counter(pat))    




# https://leetcode.com/problems/find-all-anagrams-in-a-string/
# This is leetcode question similar as above queastion
from collections import Counter
# s="usjgmhcmhgdnmphnqkamhurktrffaclvgrzkkldacl"
# p="lteojomonxrqyjzginrnnzwacxxaedrwudxzrfu"

s = "cbaebabacd"
p = "abc"
d=Counter(p)
k=len(p)
count=len(d) #taking the number of different letters present in pattern. So that when if turns to 0, we can fetch the index.
i=0
j=0
ans=[]

#First increase the j to make the slider size k. ie j-i+1=k
#Then check for count. If it is zero we take the value of i.
while(j<len(s)):

    if s[j] in d:    
        d[s[j]]-=1
        if d[s[j]]==0:
            count-=1

    if(j-i+1<k):
        j+=1

    #When slider hits the size k
    elif (j-i+1==k):
        if count==0:
            ans.append(i)
        #While shifting we need to revome the ith element so that the size remain fixed. 
		#We also need to update the value of count if required.
        if s[i] in d:
            d[s[i]]+=1
            if d[s[i]]==1:
                count+=1
        i+=1
        j+=1
print(ans)




# --------------Question 4 subarray sum is equal to k



#this is the solution if all the elements of the array is Positive only
nums = [1,3,-1,-3,5,3,6,7]
k = 3
# Output: [3,3,5,5,6,7]
i=0
j=0
l=[]
ans=[]

while (j<len(nums)):

    #calculation

    while((len(l) >0) and (l[-1]<nums[j])):
        l.pop()
    l.append(nums[j])

    if (j-i+1)<k:
        j+=1

    else:
        if (j-i+1)==k:
            ans.append(l[0])
            if (l[0]==nums[i]):
                l.pop(0)
            i+=1
            j+=1
print(ans)

# ---- this is leetcode problem solution for subarray sum is equal to k
#----- this solution is for if both negative and positive elements are presnet in arrat
class Solution:
    def subarraySum(self, arr: List[int], Sum: int) -> int:
        n=len(arr)
        # Dictionary to store number of subarrays 
        # starting from index zero having  
        # particular value of sum. 
        prevSum = defaultdict(lambda : 0)
        res = 0 
        # Sum of elements so far. 
        currsum = 0 
        for i in range(0, n):  

            # Add current element to sum so far. 
            currsum += arr[i] 

            # If currsum is equal to desired sum, 
            # then a new subarray is found. So 
            # increase count of subarrays. 
            if currsum == Sum:  
                res += 1         

            # currsum exceeds given sum by currsum  - sum.
            # Find number of subarrays having  
            # this sum and exclude those subarrays 
            # from currsum by increasing count by  
            # same amount. 
            if (currsum - Sum) in prevSum:
                res += prevSum[currsum - Sum] 


            # Add currsum value to count of  
            # different values of sum. 
            prevSum[currsum] += 1 

        return res



# -------Question 5 larget subarray with k unique characters ----

--similar Q--
1. longest substring with without repeating char
2. leetcode :-Fruit Into Baskets
