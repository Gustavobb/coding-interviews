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
Hints that were not necessary:

* A valid square has four equal sides with positive length and four equal angles (90-degree angles). 

* There're at least 4 possible ways to solve the problem.

* The input can come at any order, but does it really matter?

Necessary hints:

* Try to think how pythagorean theorem can help.

* The distance between two points is (p0.x - p1.x)^2 + (p0.y - p1.y)^2

Hints that I found useful along the way:

* The squares are not always axis aligned

* What are the possible ways to define a square? Your solution must be based on that

* A square must be made by two triangles.

* Time and space complexity are constant even at the worst case.

* Hypotenuse is the greater distance and cathetus is the smallest in a square.

* Two is the max number of possible distances in a square.

## Solution

<!-- Solution to the problem. -->
Form a list of the four points inputted. Iterate over those points two times, because you need to calculate the distance between two points. Once you have that, keep track of the largest value and the shortest value. If it is a square, the largest value (hypotenuse) should be equal to the smallest value squared (cathetus). So just return that comparison. If it is not a square, the comparison will be false.

## Time and space complexity

<!-- Time and space complexity of the solution. -->
Constant number of permutations(4!) are generated.

* Time complexity: O (1)

* Space complexity: O (1)

## Skills needed to solve the problem

<!-- Skills needed to solve the problem. -->
A lot of debugging to test the solution with different cases, because in most of the times there were a example that could potentially not work. Math skills. Depending on the solution purposed sorting and set manipulation.

## Most common mistakes

<!-- Most common mistakes. -->
The most common mistakes that I've encountered can be listed below:

* A square is formed by four equal distance lengths: That's not entirely true if you don't know the order od the points.

* Check if it's a valid square just by seeing if x equals to any other x and if y equals to any other y: This solution stops working when a non axis aligned square appears.

* Save the distances in a set, then checking if that set has only 2 elements in it: Since we are calculating floats, the hash of each distance can vary even with same distances, no one thought that an epsilon was needed in that case.

* Not being able to come up with examples of how the solution might work. Testing it with more extreme cases often would brake the proposed solution.

* Trouble with maths and geometry: That topic varied between not remembering on how to calculate a hypotenuse, how to simplify an equation and how to find the distance between two points. Also in some cases people would be very confused with square roots.

* A lot of people would consider the hypotenuse as being useful, but only a few managed to extract the best solution out of this, most people would just get stuck in how to use this data to solve the problem efficiently.

## Positive and negative points in the interviewees

<!-- Positive and negative points in the interviewees -->
Interviewing people with this same problem helped me identify who had more knowledge in maths, and who were capable of identifying a valid solution right away. There were people that thought about using the hypotenuse and that saved a lot of interview time. Others were stuck because the path they were taking was not the right one.

## What called my attention in the interviews

<!-- What called my attention in the interviews -->
I've interviewed 6 people. But only one managed to solve the problem almost the same way I did, that I consider it to be one of the best solutions. The person was able to identify the hypotenuse importance right away and use it as a tool to find if the square was valid or not. The solution that was given was optimal and was able to solve the problem with all the possible cases. 

Many people struggled with what to do with the hypotenuse and shifted the solution to checking if the number of total distances found was equal to two. This has a downside, floats are not always the same even when the calculus is done with the same values.

There was one person that manages to calculate the distance between two points without me telling that they can consider that a made up function exists and to that for them.

All of the people found the problem very interesting, even though they were not a big fan of maths.