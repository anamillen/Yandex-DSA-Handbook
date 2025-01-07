"""
Заданы n точек на прямой.

Выведите минимальную длину k отрезков, покрывающих все точки. 
Отметим, что отрезки могут иметь нулевую длину.
"""

def min_sum_of_segments(N_POINTS, MAX_SEGMENTS, points):
    """Returns the minimum sum of lengths of k segments needed to cover all the points"""
    points = sorted(points)
    distances = sorted([points[i+1]-points[i] for i in range(N_POINTS-1)], reverse=True)
    segment_sum = points[-1] - points[0]
    segment_count = 1
    ind_max_dist = 0
    # while we still have spare segments to use we can 'cut' the segments which cover the greatest distances 
    while segment_count<MAX_SEGMENTS and ind_max_dist<N_POINTS-1:
        segment_sum-=distances[ind_max_dist]
        ind_max_dist+=1
        segment_count+=1
    # from here on out we have used up all k segments (segment_count==MAX_SEGMENTS)
    # or we already have 'cut' all the distances (ind_max_dist==N_POINTS-1)
    return segment_sum

# main program
n_points, n_segments = [int(x) for x in input().split()]
points = [int(x) for x in input().split()]
print(min_sum_of_segments(N_POINTS=n_points, MAX_SEGMENTS=n_segments, points=points))
