class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)

        while len(stones)>1:
            t1=heapq.heappop_max(stones)
            t2=heapq.heappop_max(stones)
            if t1>t2:
                heapq.heappush_max(stones,t1-t2)
            else:
                continue

        return stones[0] if stones else 0