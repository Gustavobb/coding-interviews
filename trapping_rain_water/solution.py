# https://leetcode.com/problems/trapping-rain-water/
# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

# Input: height = [4,2,0,3,2,5]
# Output: 9

def trap(height: list[int]) -> int:
    """
    Return the amount of water trapped by a list of heights
    """
    p_left = 0
    p_right = len(height) - 1
    left_max = 0
    right_max = 0
    trapped_water = 0
    
    while p_left < p_right:
        if height[p_left] < height[p_right]:
            if height[p_left] >= left_max: left_max = height[p_left]
            else: trapped_water += left_max - height[p_left]
            p_left += 1
            continue
        
        if height[p_right] >= right_max: right_max = height[p_right]
        else: trapped_water += right_max - height[p_right]
        p_right -= 1 
    
    return trapped_water

def main() -> int:
    """
    Main function
    """
    assert trap([0,1,0,2,1,0,1,3,2,1,2,1]) == 6
    assert trap([4,2,0,3,2,5]) == 9

    return 0

if __name__ == "__main__":
    exit(main())