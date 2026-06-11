class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        freq={}
        for num in nums:
            freq[num]=freq.get(num,0)+1
        for n in nums:
            if freq[n]>1:
                return n
        return -1
        