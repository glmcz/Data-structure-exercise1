from typing import List


# Input: height = [0,2,0,3,1,0,1,3,2,1]
#
# Output: 9

#two pointer approach
def trap_effective_memory_approach(height: List[int]) -> int:
    max_left = 0
    max_right = 0
    left = 0
    right = len(height) - 1
    total_water = 0
    # until left and right pointer meet each other
    while left < right:
        # determine with pointer should move
        # it doesn't matter which one move if they are equal
        # but always move with smaller, because no matter of how big is boundaries on
        # one side if other side is smaller the water will flow away.
        if max_left <= max_right:
            # move left
            left += 1
            current_water = max_left - height[left]
            if current_water > 0:
                total_water += current_water
            max_left = max(height[left], max_left)
        else:
            right-= 1
            current_water = max_right - height[right]
            if current_water > 0:
                total_water += current_water
            max_right = max(height[right], max_right)

    return total_water

def trap(height: List[int]) -> int:
    total_water = 0
    n = len(height)
    # create a 2 array helpers that will track  the highest height of water from left and right
    # Left[i] contains height of tallest bar to the
    # left of i'th bar including itself
    left = [0] * n

    # Right[i] contains height of tallest bar to
    # the right of i'th bar including itself
    right = [0] * n

    # Fill left array
    left[0] = height[0]
    for i in range(1, n):
        left[i] = max(left[i - 1], height[i])

    # Fill right array
    right[n - 1] = height[n - 1]
    for i in range(n - 2, -1, -1):
        right[i] = max(right[i + 1], height[i])

    for index in range(1, n - 1):
        minOf2 = min(left[index - 1], right[index + 1])
        if minOf2 > height[index]:
            total_water += minOf2 - height[index]

    return total_water



if __name__ == '__main__':
    print(trap_effective_memory_approach([0, 2, 0, 3, 1, 0, 1, 3, 2, 1]))
    # print(trap([0, 2, 0, 3, 1, 0, 1, 3, 2, 1]))
