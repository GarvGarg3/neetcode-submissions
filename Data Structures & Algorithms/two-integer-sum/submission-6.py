class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        unsorted_nums = nums
        nums = sorted(nums)
        n = len(nums)
        k = 0
        check = 0
        while n>k:
            check=nums[n-1]+nums[k]
            if target<check:
                n-=1
            elif target>check:
                k+=1
            else:
                if nums[k] == nums[n-1]:
                    a = unsorted_nums.index(nums[k])
                    unsorted_nums.remove(nums[k])
                    b = unsorted_nums.index(nums[n-1])
                    return [a,b+1]
                a, b = unsorted_nums.index(nums[k]), unsorted_nums.index(nums[n-1])
                if a<b:
                    return [a,b]
                return [b, a]
            