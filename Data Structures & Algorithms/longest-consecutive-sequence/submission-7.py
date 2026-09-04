class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_=1
        curr=1
        
        nums=list(set(nums))
        nums.sort()
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]+1:
                curr+=1
                max_=max(curr,max_)
            else:
                curr=1
        max_=max(curr,max_)
        return max_ if len(nums)>=1 else 0