<!-- index.md: a Markdown file with your problem. It must contain at least:
Description of the problem;
Reference (where did this problem come from - remember to always give credit to other people's work);
Hints;
Solution (without code);
Time and space complexity. -->

## Problem description

<!-- Description of the problem. -->
Given the coordinates of four points in 2D space p1, p2, p3 and p4, return true if the four points construct a square. The coordinate of a point pi is represented as [xi, yi]. The input is not given in any order.

## Examples
<!-- Examples -->
```
Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
Output: true

Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,12]
Output: false

Input: p1 = [1,0], p2 = [-1,0], p3 = [0,1], p4 = [0,-1]
Output: true
```

## References

<!-- Where did this problem come from? -->
https://leetcode.com/problems/valid-square/description/

## Hints

<!-- Hints for solving the problem. -->
* A valid square has four equal sides with positive length and four equal angles (90-degree angles).
* There're at least 4 possible ways to solve the problem.
* Try to think how pythagorean theorem can help.
* The input can come at any order, but does it really matter?
* The distance between two points is (p0.x - p1.x)^2 + (p0.y - p1.y)^2

## Solution

<!-- Solution to the problem. -->
Form a list of the four points inputted. Iterate over those points two times, because you need to calculate the distance between two points. Once you have that, keep track of the largest value and the shortest value. If it is a square, the largest value (hypotenuse) should be equal to the smallest value squared (cathetus). So just return that comparison. If it is not a square, the comparison will be false.

## Time and space complexity

<!-- Time and space complexity of the solution. -->
Constant number of permutations(4!) are generated.
* Time complexity: O (1)
* Space complexity: O (1)