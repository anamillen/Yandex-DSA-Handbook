"""
Вор пробрался в лавку специй и нашел там n видов специй. 

В его рюкзак можно сложить до W фунтов, поэтому забрать все он не сможет. 
Предположим, в лавке находится wi​ фунтов специй с номером i и стоимостью ci​ долларов.

Как унести максимально дорогую добычу?
"""

# Unfortunately, even though the logic for this recursive approach seems to be fine
# It doesn't pass the tests, probably, because of the maximum recursion depth in Python
# Oh well

def max_loot(capacity, weights, costs):
    """Returns the total cost of the most expensive spices stolen"""
    if capacity==0 or len(weights)==0:
        total = 0
    else:   # if there is space in the backpack and there are still spices to choose from
        best_spice, cost_per_w = the_best_spice(weights, costs)
        amount = min(capacity, weights[best_spice])
        total = cost_per_w * amount
        weights.pop(best_spice)
        costs.pop(best_spice)
        total = total + max_loot(capacity-amount, weights, costs)
    return total

def the_best_spice(weights, costs):
    """Returns the index of the most expensive spice and its cost"""
    best_spice_i = 0; cost_per_w = costs[0]/weights[0] 
    for i in range(1, len(weights)):
        curr_cost = costs[i]/weights[i]
        if curr_cost>cost_per_w:
            cost_per_w = curr_cost
            best_spice_i = i
    return best_spice_i, cost_per_w

# main program
n, capacity = [int(x) for x in input().split()]
weights = []; costs = []
for _ in range(n):
    c, w = [int(x) for x in input().split()]
    costs.append(c)
    weights.append(w)
total = max_loot(capacity, weights, costs)
print('%.6f' % total)