class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        nums=[[nums[i],i] for i in range(len(nums))]
        heapq.heapify(nums)
        for i in range(k):
            top,idx=heapq.heappop(nums)
            heapq.heappush(nums,[top*multiplier,idx])
        res=[0 for i in range(len(nums))]
        for i in nums:
            res[i[1]]=i[0]
        return res
        