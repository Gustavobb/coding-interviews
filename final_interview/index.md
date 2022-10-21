<!-- index.md: a Markdown file with your problem. It must contain at least:
Description of the problem;
Reference (where did this problem come from - remember to always give credit to other people's work);
Hints;
Solution (without code);
Time and space complexity. -->

## Problem description

<!-- Description of the problem. -->
Given a circle represented as (radius, x_center, y_center) and an axis-aligned rectangle represented as (x1, y1, x2, y2), where (x1, y1) are the coordinates of the bottom-left corner, and (x2, y2) are the coordinates of the top-right corner of the rectangle.

Return true if the circle and rectangle are overlapped otherwise return false.

## Examples
<!-- Examples -->
```
Input: radius = 1, x_center = 0, y_center = 0, x1 = 1, y1 = -1, x2 = 3, y2 = 1
Output: true

Input: radius = 1, x_center = 1, y_center = 1, x1 = 1, y1 = -3, x2 = 2, y2 = -1
Output: false
```

## References

<!-- Where did this problem come from? -->
https://leetcode.com/problems/circle-and-rectangle-overlapping/description/

## Hints

<!-- Hints for solving the problem. -->
* Overlapped means that there is a point (xi, yi) that belongs to the circle and the rectangle at the same time.
* Drawing possibles cases and finding a geometry property may come in hand.
* It all comes down to a geometry/math problem.
* How can you find the rectangle center? Why it may help?
* Try to think how calculating the distance between the centers can help.

## Solution

<!-- Solution to the problem. -->
You need to calculate the coordinates from the centre of the rectangle first. Then, get the distance between the center of the circle and the just calculated centre of the rectangle. Calculate half the length of the rectangle. Subtract the distance between centers from the half rectangle length. Once you do that you can tell if there's any point inside both the circle and the rectangle by comparing the magnitude of x, y resulting vector to the radius os the circle. If the radius is larger that means that the rectangle has to be close enough to share at least one point with the circle.

## Time and space complexity

<!-- Time and space complexity of the solution. -->
* Time complexity: O(1)
* Space complexity: O(1)