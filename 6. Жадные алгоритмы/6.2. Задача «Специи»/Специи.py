"""
Вор пробрался в лавку специй и нашел там n видов специй. 

В его рюкзак можно сложить до W фунтов, поэтому забрать все он не сможет. 
Предположим, в лавке находится wi​ фунтов специй с номером i и стоимостью ci​ долларов.

Как унести максимально дорогую добычу?
"""

def max_loot(capacity, spices, n):
    """Returns the total cost of the most expensive spices stolen"""
    i = 0; total = 0
    spices = sorted(spices, key=lambda spice: spice['cost']/spice['weight'], reverse=True)
    while capacity>0 and i<n:
        price = spices[i]['cost']/spices[i]['weight']
        amount = min(capacity, spices[i]['weight'])
        total += price*amount
        capacity-=amount
        i+=1
    # from here on out it's either capacity==0 or i==n
    return total

# main program
n, capacity = [int(x) for x in input().split()]
spices = []
for _ in range(n):
    cost, weight = [int(x) for x in input().split()]
    spices.append({'cost':cost, 'weight':weight})
total = max_loot(capacity, spices, n)
print('%.6f' % total)