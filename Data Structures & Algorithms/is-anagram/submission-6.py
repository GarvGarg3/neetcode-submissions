class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        ls = list(s)

        for i in t:
            if i not in ls:
                return False
            ls.remove(i)
        return True

        