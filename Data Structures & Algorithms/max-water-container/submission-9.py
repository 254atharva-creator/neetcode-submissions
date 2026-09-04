class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L=0
        R=len(heights)-1
        max_=0
        while L<R:
            max_=max(max_,min(heights[R],heights[L])*(R-L))
            if heights[L]<=heights[L+1] and L+1<R:
                max_=max(max_,heights[L])
                L+=1
                
            elif heights[R]<=heights[R-1] and R-1>L:
                max_=max(max_,heights[R])
                R-=1
                
                
            else:
                
                if heights[R]>=heights[L]:
                    L+=1
                else:
                    R-=1
                
                
        return max_
            
            