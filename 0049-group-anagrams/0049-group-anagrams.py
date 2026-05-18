class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans={}
        for i in strs:
            j="".join(sorted(i))
            if j in ans:
                ans[j].append(i)
            else:
                ans[j]=[i]
        return list(ans.values())
            
                

        
        
        