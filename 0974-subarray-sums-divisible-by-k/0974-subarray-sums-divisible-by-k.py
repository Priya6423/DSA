class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        seen={0:1}
        prefix=0
        count=0
        for num in nums:
            prefix+=num
            if prefix%k in seen:
                count+=seen[prefix%k]
                seen[prefix%k]+=1
            else:
                seen[prefix%k]=1
        return count
        