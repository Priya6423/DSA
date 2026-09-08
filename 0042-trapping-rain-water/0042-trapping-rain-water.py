class Solution:
    def trap(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        leftmax=0
        rightmax=0
        ans=0
        while l<r:
            if height[l]<height[r]:
                leftmax=max(height[l],leftmax)
                ans+=leftmax-height[l]
                l+=1
            else:
                rightmax=max(height[r],rightmax)
                ans+=rightmax-height[r]
                r-=1
        return ans

        