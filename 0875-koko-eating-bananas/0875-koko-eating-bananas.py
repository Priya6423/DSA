class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low=1
        high=max(piles)
        def ispossible(mid,piles,h):
            sum=0
            for i in piles:
                sum+=ceil(i/mid)
            if sum<=h:
                return True
            return False

        while(low<high):
            mid=low+(high-low)//2
            if ispossible(mid,piles,h):
                high=mid
            else:
                low=mid+1
        return low
            
