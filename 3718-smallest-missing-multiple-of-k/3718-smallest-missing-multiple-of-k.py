class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        num=set(nums)
        for i in range(k,k*50,k):
            if i not in num:
                return i
        return nums[-1]+k


 