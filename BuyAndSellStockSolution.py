class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        high = 0
        low = 10000
        i = 0
        """Theory:
        search for the highest int succeeding the absolute min of the array
        return the difference between these two values 
        """

        for price in prices:
            if price <= low:
                low = price
            else:
                profit = price - low
                if profit > high:
                    high = profit
        return high