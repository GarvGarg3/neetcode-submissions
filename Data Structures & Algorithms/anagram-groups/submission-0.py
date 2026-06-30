class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped = []
        seen = {}
        for ch in strs:
            a = sorted(ch)
            key = ''.join(a)
            if key not in seen:
                seen[key] = []
            seen[key].append(ch)

        return list(seen.values())