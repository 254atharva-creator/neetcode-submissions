class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L=0
        R=len(nums)-1
        while L<=R:
            X=L+(R-L)//2
            if nums[X]==target:
                return X
            elif nums[X]>target:
                R=X-1
            elif nums[X]<target:
                L=X+1
        return -1