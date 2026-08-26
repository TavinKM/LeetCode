class Solution(object):
    def finalPrices(self, prices):
        results = prices
        for i in range(len(prices)):
            n = i + 1
            while n < len(prices):
                if prices[n] <= prices[i]:
                    results[i] = prices[i] - prices[n]
                    break
                n += 1
        return results
        