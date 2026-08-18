class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen={}
        maxi=0
        for i in range(len(nums)):
            seen[nums[i]]=True
        for num in nums:
            if num-1 not in seen:
                length=1
                while length+num in seen:
                    length+=1
                if length>maxi:
                    maxi=length
        return maxi

                

                


        