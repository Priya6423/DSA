class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        res=[]
        def backtrack(start,remaining,path):
            if remaining==0:
                res.append(path[:])
            for i in range(start,len(candidates)):
                if i>start and candidates[i-1]==candidates[i]:
                    continue
                if candidates[i]>remaining:
                    break
                path.append(candidates[i])
                backtrack(i+1,remaining-candidates[i],path)
                path.pop()
        backtrack(0,target,[])
        return res
