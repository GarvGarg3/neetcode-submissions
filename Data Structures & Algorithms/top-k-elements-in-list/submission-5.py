class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}

        for i in nums:
            seen[i] = seen.get(i, 0) + 1

        num = []

        while len(num) != k:
            max_key = max(seen, key=seen.get)
            num.append(max_key)
            seen.pop(max_key)

        return num
                    