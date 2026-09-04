class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()
        for i in range(len(nums)-1):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            target=-1*nums[i]
            L=i+1
            R=len(nums)-1
            while L<R:
                if nums[L]+nums[R]==target:
                    res.append([nums[i],nums[L],nums[R]])
                    L+=1
                    R-=1
                    while nums[L] == nums[L - 1] and L < R:
                        L += 1
                elif nums[L]+nums[R]<target:
                    L+=1
                elif nums[L]+nums[R]>target:
                    R-=1
        return res


