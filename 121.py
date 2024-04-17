class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        buy_date = 0
        sell_date = 1

        for i in range(len(prices) - 1):
            profit = prices[sell_date] - prices[buy_date]
            if profit < 0:
                buy_date = sell_date
            elif profit > max_profit:
                max_profit = profit
            sell_date += 1
        return max_profit

        # max_profit = 0
        # max_sub_prices = [0] * (len(prices) - 1)
        #
        # for i in range(len(prices) - 1):
        #     if i != 0 and max_sub_prices[i - 1] > i:
        #         max_sub_prices[i] = max_sub_prices[i - 1]
        #     else:
        #         sub_prices = prices[i + 1:len(prices)]
        #         max_sub_prices[i] = prices.index(max(sub_prices))
        #     profit = prices[max_sub_prices[i]] - prices[i]
        #     max_profit = max(max_profit, profit)
        # return max_profit
