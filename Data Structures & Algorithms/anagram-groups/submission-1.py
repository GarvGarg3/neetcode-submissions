class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen={}
        sorted_ls=[]
        result=[]
        for i in range(len(strs)):
            var1=strs[i].split()
            sorted_var = "".join(sorted(strs[i]))
            sorted_ls.append(sorted_var)
        for i, val in enumerate(sorted_ls):
            if val not in seen:
                seen[val]=[i]
            else:
                seen[val].append(i)
        for keys in seen:
            ls=[]
            for i in seen[keys]:
                ls.append(strs[i]) 
            result.append(ls)
        return result