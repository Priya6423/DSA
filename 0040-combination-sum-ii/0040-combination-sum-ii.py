class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result=[]
        path=[]
        def combine(start,remaining):
            if remaining==0:
                result.append(path[:])
            if remaining<0:
                return
            for i in range(start,len(candidates)):
                if i>start and candidates[i]==candidates[i-1]:
                    continue
                path.append(candidates[i])
                combine(i+1,remaining-candidates[i])
                path.pop()
        combine(0,target)
        return result


        