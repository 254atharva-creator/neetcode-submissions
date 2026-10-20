import math
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        heapq.heapify_max(gifts)
        for i in range(k):
            top=heapq.heappop_max(gifts)
            heapq.heappush_max(gifts,int(math.sqrt(top)))
        return sum(gifts)