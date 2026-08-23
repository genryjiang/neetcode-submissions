class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # indexes
        buy = 0
        sell = 1
        profit = 0
        while (sell < (len(prices))):
            #print("looking at buy: " + str(prices[buy]))
            #print("looking at sell: " + str(prices[sell]))
            if (prices[buy] > prices[sell]):
                # if our buy price is higher than sell, move buy pointer
                buy = sell
                sell = buy + 1
                continue;
                # greedy, move pointer to this local low
            if (prices[buy] < prices[sell]):
                # move take profit, compare profit, keep highest profit
                temp = prices[sell]-prices[buy]
                # print("curr profit: " + str(profit))
                # print("curr calc: " + str(temp))
                if profit < temp:
                    profit = temp
            # regardless, move pointer
            sell +=1 
        return profit

            