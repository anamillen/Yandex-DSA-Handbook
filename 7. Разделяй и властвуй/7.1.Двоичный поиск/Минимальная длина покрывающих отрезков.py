"""
Заданы n точек на координатной прямой. 
Вам требуется покрыть все точки на прямой k отрезками одинаковой длины.

Необходимо определить, какую минимальную длину могут иметь отрезки.
"""

def min_len_of_segments(N_POINTS, MAX_SEGMENTS, points):
    """Returns the minimum length of k segments to cover all the points"""
    points = sorted(points)
    all_covered = False
    segment_len = 0
    while not all_covered:
        i_point = 0
        segment_count = 0
        while segment_count<MAX_SEGMENTS and i_point<N_POINTS:
            covered_to = points[i_point]+segment_len
            while i_point<N_POINTS and points[i_point]<=covered_to:
                i_point+=1
            # from here on out we have moved further by 1 segment
            segment_count+=1
        # from here on out we have laid all the k segments
        if i_point==N_POINTS and segment_count<=MAX_SEGMENTS:   # if we have covered all the points then
            all_covered = True
        else:   # if not, we increment the segment length
            segment_len+=1
    # from here on out we have covered all the points (all_covered==True) with k (or less) segments
    return segment_len

# main program
n_points, n_segments = [int(x) for x in input().split()]
points = [int(x) for x in input().split()]
print(min_len_of_segments(N_POINTS=n_points, MAX_SEGMENTS=n_segments, points=points))