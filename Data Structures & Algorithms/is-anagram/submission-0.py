class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def hasher(s):
            hashmap={}
            for i in s:
                if i in hashmap:
                    hashmap[i]+=1
                else:
                    hashmap[i]=1
            return hashmap
        if hasher(s)==hasher(t):
            return True
        else:
            return False
        

                