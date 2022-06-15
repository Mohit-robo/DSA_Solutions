'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

'''


class Solution:
    def maxProfit(prices: list) -> int:
        
        min_price = float('inf')
        print(min_price)
        max_prof = 0
        for price in prices:
            print("Price:",price)
            min_price = min(min_price,price)
            print('MIN',min_price)
            max_prof = max(max_prof,price - min_price)
            print('MAX',max_prof)
        return max_prof


# prices = [7,1,5,3,6,4]
# prices = [7,5,3,6,1,4]
# prices = [2,4,1]
# prices = [7,6,4,3,1]
# prices = [3,3]
prices = [2,1,2,0,1]
print(Solution.maxProfit(prices))