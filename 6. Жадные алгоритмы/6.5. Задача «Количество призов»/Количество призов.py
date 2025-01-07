"""
Вы занимаетесь организацией соревнований для детей, и у вас есть n конфет, которые вы раздадите в качестве призов. 
Вы хотите отдать эти конфеты тем, кто займет первые k мест в соревнованиях, и распределить конфеты так, чтобы за более высокое место всегда выходило больше конфет.

Чтобы порадовать как можно больше детей, вам понадобится найти самое большое значение k, при котором это возможно.
"""

def arithmetic_sum(n):
    """Returns the value of the sum 1+2+3+...+n"""
    return (n * (n+1)) / 2

def max_prizes(N_CANDIES):
    """Returns the largest possible value of places with different prizes"""
    n_places = 0
    while arithmetic_sum(n_places+1)<=N_CANDIES:
        n_places+=1
    # from here on out there is no way we can give different prizes to every place (arithm_sum>=N_CANDIES)
    return n_places

# main program
n_candies = int(input())
print(max_prizes(N_CANDIES=n_candies))