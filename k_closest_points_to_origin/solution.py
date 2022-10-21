# https://leetcode.com/problems/k-closest-points-to-origin/description/

# Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).
# The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).
# You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

# Input: points = [[1,3],[-2,2]], k = 1
# Output: [[-2,2]]
# Explanation:
# The distance between (1, 3) and the origin is sqrt(10).
# The distance between (-2, 2) and the origin is sqrt(8).
# Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
# We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].

# Input: points = [[3,3],[5,-1],[-2,4]], k = 2
# Output: [[3,3],[-2,4]]
# Explanation: The answer [[-2,4],[3,3]] would also be accepted.

def k_closest(points: list[list[int]], k: int) -> list[list[int]]:
    """
    Find the k closest points to the origin.
    """
    dicts = dict()

    for p in points:
        dicts.setdefault(dist_points_origin(p), list()).append(p)

    answer = list()
    dicts = dict(sorted(dicts.items(), key=lambda item: item[0]))

    for dist in dicts:
        for i in dicts[dist]:
            if k <= 0: return answer
            answer.append(i)
            k -= 1

    return answer

def dist_points_origin(point1: list[int]):
    """
    Calculate the distance between two points.
    """
    return ((point1[0] - 0) ** 2 + (point1[1] - 0) ** 2)

def main() -> int:
    """
    Main function
    """
    assert k_closest([[1, 3], [-2, 2]], 1) == [[-2, 2]]
    assert k_closest([[3, 3], [5, -1], [-2, 4]], 2) == [[3, 3], [-2, 4]]

if __name__ == "__main__":
    exit(main())