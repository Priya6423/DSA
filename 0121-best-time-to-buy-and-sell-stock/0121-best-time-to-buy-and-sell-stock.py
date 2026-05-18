class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        maxi=0
        best=prices[0]
        for i in prices:
            if i<=best:
                best=i
            else:
                profit=i-best
                maxi=max(profit,maxi)
        return maxi


        