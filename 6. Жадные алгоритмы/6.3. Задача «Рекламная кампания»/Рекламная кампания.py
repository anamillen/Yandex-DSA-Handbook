"""
У вас есть популярная страница в интернете, на которой есть n рекламных мест. Вы хотите продать их рекламодателям. 
Аналитики рассчитывают на clicks1​, clicks2​, … clicksn​ кликов в день, соответственно.

С вами связались n рекламодателей, которые готовы заплатить price1​, price2​, … pricen​ за клик.

Как подобрать пары рекламных мест и рекламодателей так, чтобы получить максимальную прибыль?
"""

def max_profit(n, clicks, prices):
    """Returns the maximum profit obtained from optimal pairs of
    advertising slots and advertisers
    (prices and clicks are the same length n)"""
    clicks.sort(reverse=True)   # reversing just in sure
    prices.sort(reverse=True)   # if initial conditions are respected, there's really no need to reverse
    total = 0
    for i in range(n):
        total += clicks[i]*prices[i]
    return total

# main program
n = int(input())
clicks = [int(x) for x in input().split()]
prices = [int(x) for x in input().split()]
print(max_profit(n, clicks=clicks, prices=prices))