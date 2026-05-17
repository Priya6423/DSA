class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        my_set=set(nums)
        return len(nums)!=len(my_set)
        