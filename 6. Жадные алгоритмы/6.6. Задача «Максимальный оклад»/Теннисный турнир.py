"""
В теннисном турнире принимают участие n роботов-спортсменов. Про каждого из них известно, насколько хорошо он играет. 
Умение i-го робота описывается числом ai​. В игре двух роботов всегда побеждает тот, у кого умение играть в теннис больше. 
В этой задаче мы будем полагать, что все значения ai​ различны.

В каждом раунде теннисного турнира роботы разбиваются на пары. Если количество продолжающих участие в турнире нечетное, 
то один из роботов без игры проходит в следующий раунд. После игры в каждой из пар, в следующий раунд выходит победитель, 
а проигравший выбывает из турнира.

Определите, какое наибольше количество игр в турнире может выиграть k-й робот-спортсмен.
"""

def max_tours(n_robots, ROBOT, robots):
    """Returns the maximum number of tournaments in which
    the robot with number ROBOT can participate"""
    the_skill = robots[ROBOT]
    stronger_robots = len([robot for robot in robots if robot>the_skill])
    weaker_robots = len([robot for robot in robots if robot<the_skill])
    finished = False
    tour_counter = 0 
    if n_robots==1:
        finished = True
    while not finished:
        if stronger_robots%2==0:
            stronger_robots//=2
            weaker_robots//=2
        else:   # if the number of stronger robots is odd then
            stronger_robots = stronger_robots//2 + 1
            if weaker_robots%2==0  and weaker_robots>0:
                weaker_robots = weaker_robots//2 - 1
            else:   # if the number of weaker robots is odd then
                weaker_robots = weaker_robots//2
        n_robots = stronger_robots + weaker_robots + 1
        tour_counter += 1
        if n_robots <= 2 or (stronger_robots%2!=0 and weaker_robots==0):
            finished = True
            if weaker_robots>0:
                tour_counter += 1

    return tour_counter




# main program
N_ROBOTS, ROBOT = [int(x) for x in input().split()]
robot_skills = [int(a) for a in input().split()]

print(max_tours(n_robots=N_ROBOTS, ROBOT=ROBOT-1, robots=robot_skills))

