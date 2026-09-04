class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        pref=[1]*(n)
        preffix=1
        for i in range(1,n):
            pref[i]=preffix=nums[i-1]*preffix
        suff=[1]*n
        suffix=1
        for i in range(n-2,-1,-1):
            suff[i]=suffix=nums[i+1]*suffix
        res=[0]*n
        for i in range(n):
            res[i]=pref[i]*suff[i]
        return res

            

