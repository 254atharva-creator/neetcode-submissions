class Solution:
    def kClosest(self, nums: List[List[int]], k: int) -> List[List[int]]:
        arr=[(nums[i][0]**2+nums[i][1]**2,nums[i][0],nums[i][1]) for i in range(len(nums))]
        heapq.heapify(arr)
        res=[]
        for i in range(k):
            coords=heapq.heappop(arr)
            res.append(coords[1:])
        return res