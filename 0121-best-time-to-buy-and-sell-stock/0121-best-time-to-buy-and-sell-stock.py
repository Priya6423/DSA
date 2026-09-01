class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy=prices[0]
        maxi=-1
        for i in range(len(prices)):
            if prices[i]<buy:
                buy=prices[i]
            maxi=max(maxi,prices[i]-buy)
        return maxi
        