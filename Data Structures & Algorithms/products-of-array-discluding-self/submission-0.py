class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        values = {}
        zeros = []
        output = []
        total = 1
        for key, value in enumerate(nums):
            values[key] = value
        for i in range(len(values)):
            if values[i] == 0:
                zeros.append(i)
                continue
            total*=values[i]
            
        for i in range(len(nums)):
            if (len(zeros) > 1) or (len(zeros)==1 and i not in zeros):
                output.append(0)
                
            elif nums[i] == 0:
                output.append(total)
            else:
                output.append(total//nums[i])
        return output



