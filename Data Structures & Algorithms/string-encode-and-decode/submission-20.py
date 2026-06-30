class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return "None"
        return "\n".join(strs)
    def decode(self, s: str) -> List[str]:
        if s=="None":
            return []
        return s.split("\n")
