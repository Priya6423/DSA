class Solution:
    def climbStairs(self, n: int) -> int:
        prev1=0
        prev2=1
        if n<=3: return n
        while n:
            prev1,prev2=prev2,prev1+prev2
            n-=1
        return prev2

        