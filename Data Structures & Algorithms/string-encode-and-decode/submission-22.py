class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return "\x00"
        return "\n".join(strs)
    def decode(self, s: str) -> List[str]:
        if s=="\x00":
            return []
        return s.split("\n")
