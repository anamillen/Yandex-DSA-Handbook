"""Предположим, что у кассира есть бесконечное количество монет номиналами 1, 5, 10.

Найдите все наборы монет, которые в сумме дают money. Требуется вывести количество подходящих наборов монет и сами наборы.

Два набора считаются различными, если мультимножества монет не совпадают."""

def change_variations(money):
    """Returns the total amount of variations for giving the change = money
    Returns all the variations"""
    count = 0; variations = []
    for n_of10 in range(0, money//10 + 1):                  # here we're examining all the possible amounts of 10s to take
        for n_of5 in range(0, (money-10*n_of10)//5 + 1):    # when we've chosen the amount of 10s we consider all the posible combinations of 5
            n_of1 = money - 10*n_of10 - 5*n_of5             # we calculate the amount of 1s
            if n_of1>=0:    # if we get a good sum we add the solution
                count+=1
                variations.append((n_of10, n_of5, n_of1))
    return count, variations

# main program
money = int(input())
num_var, vars = change_variations(money)
print(num_var)
for var in vars:
    print(sum(var), end="")
    print(var[0]*" 10", end="")
    print(var[1]*" 5", end="")
    print(var[2]*" 1")

