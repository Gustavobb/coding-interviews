# https://leetcode.com/problems/course-schedule-ii/description/
# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: [0,1]
# Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].

# Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
# Output: [0,2,1,3]
# Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
# So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].

# Input: numCourses = 1, prerequisites = []
# Output: [0]

# 1 <= numCourses <= 2000
# 0 <= prerequisites.length <= numCourses * (numCourses - 1)
# prerequisites[i].length == 2
# 0 <= ai, bi < numCourses
# ai != bi
# All the pairs [ai, bi] are distinct.

def find_order(numCourses: int, prerequisites: list[list[int]]) -> list[int]:
    '''
    Find the order of courses to take to finish all courses.
    '''
    # Build a graph of dependencies
    dependencies = dict()
    for course, dep in prerequisites:
        dependencies.setdefault(course, set()).add(dep)

    # Add to answer courses
    answer = list()
    visited = set()
    for course in range(numCourses):
        if course not in visited and not dfs(course, visited, answer, dependencies):
            return list()

    return answer

def dfs(course: int, took: set[int], order: list[int], prereq: dict[int, list[int]]) -> bool:
    '''
    Depth-first search
    '''
    took.add(course)
    for dep in prereq.get(course, []):
        if dep not in took:
            if not dfs(dep, took, order, prereq):
                return False
        elif dep in order:
            return False
    order.append(course)
    return True

def main() -> int:
    '''
    Main function
    '''
    assert find_order(2, [[1, 0]]) == [0, 1]
    assert find_order(4, [[1, 0], [2, 0], [3, 1], [3, 2]]) == [0, 2, 1, 3]
    assert find_order(1, []) == [0]
    return 0

if __name__ == '__main__':
    exit(main())