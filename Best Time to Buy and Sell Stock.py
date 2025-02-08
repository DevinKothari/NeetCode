#https://neetcode.io/problems/buy-and-sell-crypto
#Brute Force solution
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        count = 0
        res = {} 

        while count < len(prices):
            left = prices[count] 
            right = left  

            for i in range(count, len(prices)): 
                if prices[i] > right:
                    right = prices[i] 

            profit = right - left
            if profit > 0:
                res[count] = profit  

            count += 1  

        return max(res.values(), default=0) 