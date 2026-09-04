class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        L=0
        R=len(s)-1
        booler=True
        while L<=R:
            if s[L] not in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789":
                L+=1
                continue
            elif s[R] not in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789":
                R-=1
                continue
            elif s[L]!=s[R]:
                booler=False
            L+=1
            R-=1

        return booler
