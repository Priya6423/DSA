class Solution:
    def climbStairs(self, n: int) -> int:
        def climb(n,dp):
            if n<=2:
                return n
            if dp[n]!=-1:
                return dp[n]
            else:
                dp[n]= climb(n-1,dp)+climb(n-2,dp)
                return dp[n]
        m=n+1
        dp=[-1]*m
        ans=climb(n,dp)
        return ans

        