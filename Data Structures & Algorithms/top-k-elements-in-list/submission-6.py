
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen={}
        for num in nums:
            seen[num] = seen.get(num,0)+1
        while len(seen)!=k:
            if len(seen)<=k:
                return None
            if len(seen)==k:
                return list(seen.keys())
            seen = {k: v - 1 for k, v in seen.items()}
            for key in list(seen):
                if seen[key] == 0:
                    seen.pop(key)
        return list(seen.keys())
                    