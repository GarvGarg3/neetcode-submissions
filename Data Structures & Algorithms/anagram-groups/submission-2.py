class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen={}
        sorted_ls=[]
        result=[]
        for i in range(len(strs)):
            var1=strs[i].split()
            sorted_var = "".join(sorted(strs[i]))
            if sorted_var not in seen:
                seen[sorted_var]=[strs[i]]
            else:
                seen[sorted_var].append(strs[i])

        return list(seen.values())