class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0 
        costprice = prices[0]

        for p in prices:
            maxprofit = max(maxprofit, p - costprice)
            costprice = min(costprice, p)
        return maxprofit 

            

        
        