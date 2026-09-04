class Solution:

    def encode(self, strs: List[str]) -> str:
        s=""
        for i in strs:
            s+=f"{i}-"
        return s
    def decode(self, s: str) -> List[str]:
        return s.split("-")[:len(s.split("-"))-1]
