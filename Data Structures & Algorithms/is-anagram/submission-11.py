class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        seen={}
        for i in range(len(s)):
            seen[s[i]] = seen.get(s[i], 0) + 1
        
        for i in range(len(s)):
            if t[i] not in seen:
                return False
            else:
                if seen[t[i]]==1:
                    seen.pop(t[i], None)
                else:
                    seen[t[i]]-=1
        return True
        

        