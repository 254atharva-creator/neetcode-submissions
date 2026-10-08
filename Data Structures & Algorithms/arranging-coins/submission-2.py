class Solution:
    def arrangeCoins(self, n: int) -> int:
        i=0;
        if n==1:return 1
        while i*(i+1)/2<n:
            i+=1
        return i-1