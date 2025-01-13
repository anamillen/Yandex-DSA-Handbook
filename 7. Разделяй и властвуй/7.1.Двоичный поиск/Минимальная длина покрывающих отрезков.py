"""
Заданы n точек на координатной прямой. 
Вам требуется покрыть все точки на прямой k отрезками одинаковой длины.

Необходимо определить, какую минимальную длину могут иметь отрезки.
"""
def can_cover_with_k(segment_len, K, points, N_POINTS):
    """Returns a boolean indicating if all points can be covered with K segments
    of length segment_len"""
    can_cover = False
    n_segments = 0
    i_point = 0
    while n_segments < K and not can_cover:
        covered = points[i_point]
        while i_point < N_POINTS and points[i_point] <= covered + segment_len:
            i_point += 1
        # from here on out it's either i_point==N_POINTS (we have covered all the points)
        # or points[i_point] > covered + segment_len     (we need more segments)
        if i_point == N_POINTS:
            can_cover = True
        n_segments += 1

    # from here on out it's n_segments==K                (we have used up all available segments)
    # or can_cover
    return can_cover

def min_len_of_segments(MAX_SEGMENTS, points, N_POINTS):
    """Returns the minimum length of k segments to cover all the points"""
    points = sorted(points)
    # binary search bounds: lower and higher length bounds
    low = 0
    high = points[-1] - points[0]

    while low < high:
        mid = (high + low) // 2
        if can_cover_with_k(mid, MAX_SEGMENTS, points, N_POINTS):
            high = mid
        else:   # if the length is too short
            low = mid + 1
    # here low >= high

    return low  # returning the lowest distance calculated

# main program
n_points, n_segments = [int(x) for x in input().split()]
points = [int(x) for x in input().split()]
print(min_len_of_segments(N_POINTS=n_points, MAX_SEGMENTS=n_segments, points=points))