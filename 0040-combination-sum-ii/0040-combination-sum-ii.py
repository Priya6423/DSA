class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        path=[]
        ans=[]
        def backtrack(start,remaining):
            if remaining==0:
                ans.append(path[:])
            if remaining<0:
                return
            for i in range(start,len(candidates)):
                if i>start and candidates[i-1]==candidates[i]:
                    continue
                path.append(candidates[i])
                backtrack(i+1,remaining-candidates[i])
                path.pop()
        backtrack(0,target)
        return ans

        