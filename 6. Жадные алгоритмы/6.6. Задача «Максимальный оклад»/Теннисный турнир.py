"""
В теннисном турнире принимают участие n роботов-спортсменов. Про каждого из них известно, насколько хорошо он играет. 
Умение i-го робота описывается числом ai​. В игре двух роботов всегда побеждает тот, у кого умение играть в теннис больше. 
В этой задаче мы будем полагать, что все значения ai​ различны.

В каждом раунде теннисного турнира роботы разбиваются на пары. Если количество продолжающих участие в турнире нечетное, 
то один из роботов без игры проходит в следующий раунд. После игры в каждой из пар, в следующий раунд выходит победитель, 
а проигравший выбывает из турнира.

Определите, какое наибольше количество игр в турнире может выиграть k-й робот-спортсмен.
"""

def match_making(stronger_robots, weaker_robots):
    """Returns the number of stronger_robots and weaker_robots who passed to the next tournament"""
    # divide the robots into pairs. stronger robots "eliminate" each other:
    if stronger_robots % 2 == 0:
        stronger_robots //= 2   # as the number of stronger robots is pair every one gets a pair
        weaker_robots   //= 2   # if the number of weaker robots is pair, one of them gets a 'bye'
                                # if it's odd, we pair one of the weaker robots with our robot
    else:  # if the number of stronger robots is odd then
        # one of them gets a 'bye' or gets paired with a weaker robot
        # meaning their count decreases slightly less.
        stronger_robots = stronger_robots // 2 + 1
        if weaker_robots % 2 == 0:  # if the number of weaker robots is pair then
            # the total number is pair, so one more weaker robot gets eliminated by our robot
            weaker_robots = weaker_robots // 2 - 1
        else:  # if the number of weaker robots is odd then
            # one stronger robots gets a 'bye'
            weaker_robots = weaker_robots // 2
    return stronger_robots, weaker_robots

def max_tours(robot_index, skills):
    """Returns the maximum number of tournaments in which
    the robot with number robot_index+1 can participate"""
    the_skill = skills[robot_index]
    # counting the total of stronger and weaker robots
    stronger_robots = sum([1 for skill in skills if skill > the_skill])
    weaker_robots = sum([1 for skill in skills if skill < the_skill])
    tour_counter = 0
    while weaker_robots != 0:
        stronger_robots, weaker_robots = match_making(stronger_robots, weaker_robots)
        tour_counter += 1
    # from here on out, there are no more matches our robot could win. it's either:
    # our robot is the only one standing or all the other robots are stronger (weaker_robots == 0)
    return tour_counter

# main program
_, ROBOT_NUM = [int(x) for x in input().split()]
robot_skills = [int(a) for a in input().split()]
print(max_tours(robot_index=ROBOT_NUM-1, skills=robot_skills))

