"""


121. Best Time to Buy and Sell Stock
Description
Hints
Submissions
Discuss
Solution
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
 

Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 104
"""

#here we have used two pointer approach
#logic 1
def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy = 0
        sell = 1
        max_profit = 0
        while buy < len(prices) and sell < len(prices):
            profit = prices[sell]-prices[buy]
            if profit <= 0:
                buy = sell
                sell+=1
            else:
                max_profit = max(max_profit,profit)
                sell+=1
        return max_profit


#logic 2
def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy = prices[0]
        max_profit = 0
        
        for i in range(1,len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            else:
                profit = prices[i] - buy
                max_profit = max(profit,max_profit)
        return max_profit
