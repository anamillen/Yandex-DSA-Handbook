"""
Ваша задача — собрать подписи всех жильцов в доме. Вам известно время, в которое каждый из жильцов находится дома. 
Вы хотели бы собрать все подписи, приходя в дом минимальное количество раз. Для простоты давайте предположим, 
что вы сразу же собираете подписи всех жильцов, находящихся дома, когда заходите.
"""

def collect_signatures(segments):
    """Returns the minimum number of visits to make to collect all the signatures
    Returns the hours for collecting signatures"""
    n_of_visits = 0
    hours_to_visit = []
    # it can be proven mathematically that the best way to choose the hours to visit
    # is by choosing a segment which ends the earliest every time
    # and 'come' at the end of it
    segments = sorted(
        segments, key = (lambda x: x[1])
    )
    while len(segments)!=0:
        best_hour = segments[0][1]
        segments = [segments[i] for i in range(len(segments)) if segments[i][0]>best_hour]
        n_of_visits+=1
        hours_to_visit.append(str(best_hour))   # here we convert the hours directly to string format to print it easier later
    # from here on out we have covered all the segments (len(segments)==0)
    return n_of_visits, hours_to_visit

# main program
n_segments = int(input())
segments = []
for _ in range(n_segments):
    from_h, to_h = [int(x) for x in input().split()]
    segments.append((from_h, to_h))

n_of_visits, hours_to_visit = collect_signatures(segments=segments)
print(n_of_visits)
print(" ".join(hours_to_visit))