class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        for i in nums:
            if i not in freq:
                freq[i]=1
            else:
                freq[i]+=1
        lst=[]
        for i in freq:
            lst.append([i,freq[i]])
        lst=sorted(lst, key=lambda x: x[1])
        res=[]
        for i in range(len(lst)-1,len(lst)-k-1,-1):
            res.append(lst[i][0])
            lst.pop()

        return res
        