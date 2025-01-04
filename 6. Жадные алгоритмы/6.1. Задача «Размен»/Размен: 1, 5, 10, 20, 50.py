"""Предположим, что у кассира есть бесконечное количество монет номиналами 1, 5, 10, 20 и 50.

Найдите набор монет, с суммарным номиналом money, в котором наименьшее количество монет. 
Требуется вывести номиналы монет в этом наборе."""

def change(money):
    """Returns the least amount of coins needed to return change
    Returns the way to return change using as few coins as possible"""
    count = 0
    change = {50:0, 20:0, 10:0, 5:0, 1:0}
    for nominal in change:
        change[nominal]+=money//nominal
        count += change[nominal]
        money = money%nominal
    return count, change

# main program
money = int(input())
count, change = change(money)
print(count)
for nom in change:
    nom_str = str(nom)+" "
    print(nom_str*change[nom], end="")
        




