class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded=[]
        if strs == []:
            return "\x00"
        for word in strs:
            word = f"{len(word)}#{word}"
            encoded.append(word)
        return "".join(encoded)
    def decode(self, s: str) -> List[str]:
        decoded=[]
        if s=="\x00":
            return []
        while len(s)>0:
            i = s.index("#")
            n = int(s[:i])
            word = s[i + 1:i + 1 + n]
            decoded.append(word)
            s = s[i + 1 + n:]
        return decoded