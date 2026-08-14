class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeros=[]
        total=1
        result=[]
        
        for i in range(len(nums)):
            if nums[i]==0:
                zeros.append(i)
                continue
            total*=int(nums[i])
        for i in range(len(nums)):
            if len(zeros) > 1:
                result.append(0)

            elif len(zeros) == 1:
                if nums[i] == 0:
                    result.append(total)
                else:
                    result.append(0)

            else:
                result.append(total // nums[i])
        return result




