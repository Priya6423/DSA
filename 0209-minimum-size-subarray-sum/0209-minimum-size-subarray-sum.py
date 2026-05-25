class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        right=0
        left=0
        sums=nums[0]
        mini=float('inf')
        while(left<=right and right<len(nums) and left<len(nums)):
            if nums[right]>=target or nums[left]>=target:return 1
            if(sums>=target) :
                 mini=min(mini,(right+1)-left)
                 sums-=nums[left]
                 left+=1
            elif sums<target:
                if(right+1<len(nums)):
                    right+=1
                    sums+=nums[right]
                else:
                    break
        return 0 if mini == float('inf') else mini


                

