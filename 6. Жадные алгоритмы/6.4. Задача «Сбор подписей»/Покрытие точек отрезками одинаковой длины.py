"""
Заданы n точек на прямой.

Выведите наименьшее количество отрезков длины L, которые необходимы, чтобы покрыть все точки.
"""

def minimum_segments(N_POINTS, L, points):
    """Returns the minimum number of segments needed to cover all the points"""
    points = list(points)
    points.sort()   # this algorithm will only work if the list is sorted
    n_segments = 0
    i_point = 0
    while i_point<N_POINTS:
        covered_to = points[i_point]+L
        while i_point<N_POINTS and points[i_point]<=covered_to:
            i_point+=1
        # from here on out we have skipped all the points covered by 1 segment (points[i_point]>covered_to)
        n_segments+=1
    # from here on out all the points have been covered (i_point==N_POINTS)
    return n_segments

# main program
n_points, len_segment = [int(x) for x in input().split()]
points = [int(x) for x in input().split()]
print(minimum_segments(N_POINTS=n_points, L=len_segment, points=points))
