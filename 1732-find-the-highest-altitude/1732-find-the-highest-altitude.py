class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        maxi=0
        ans=0
        for i in range(len(gain)):
            ans+=gain[i]
            maxi=max(ans,maxi)
        return maxi
            

        