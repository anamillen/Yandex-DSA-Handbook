"""
В качестве последнего вопроса на собеседовании будущий начальник дает вам n бумажек с одним числом на каждой и говорит составить из них самое большое число. 
Получившееся число — ваша зарплата, поэтому вы очень замотивированы решить эту задачу!
"""

def is_better(max_num, curr_num):
    """Returns the boolean indicating if the current number (curr_num)
    is better to choose than max_num first to get the largest possible combination
    if yes - returns True, else - False"""
    answer = False
    if int(curr_num+max_num)>int(max_num+curr_num):
        answer = True
    return answer

def form_the_largest_number(numbers):
    """Returns a list with numbers from 'numbers' sorted as to 
    give the largest number possible when concatenated"""
    largest_number = ""
    while len(numbers)!=0:
        max_num = numbers[0]
        for num in numbers:
            if is_better(max_num=max_num, curr_num=num):
                max_num = num
        largest_number += max_num
        numbers.remove(max_num)
    # from here on out we have used up all the numbers
    return largest_number

# main program
n_nums = int(input())
nums = input().split()
print(form_the_largest_number(numbers=nums))
