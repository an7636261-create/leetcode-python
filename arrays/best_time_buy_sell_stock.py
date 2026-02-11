def maxprofit(prices):
    min_price=float('inf') #sets min price to infinity,I haven't chosen a buy day yet
    max_profit=0 #starts at 0 ,no loss is allowed

    for price in prices:
        if price < min_price:
            min_price = price
        else:
            profit = price - min_price
            max_profit = max(max_profit,profit)

    return max_profit

#example
print(maxprofit([7,1,5,3,6,4]))
