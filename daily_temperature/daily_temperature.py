# Daily Temperatures
# Solved
#
# You are given an array of integers temperatures where temperatures[i] represents the daily temperatures on the ith day.
#
# Return an array result where result[i] is the number of days after the ith day before a warmer temperature appears on a future day. If there is no day in the future where a warmer temperature will appear for the ith day, set result[i] to 0 instead.
#
# Example 1:
#
# Input: temperatures = [30,38,30,36,35,40,28]
#
# Output: [1,4,1,2,1,0,0]
#
# Example 2:
#
# Input: temperatures = [22,21,20]
#
# Output: [0,0,0]
#
# Constraints:
#
#     1 <= temperatures.length <= 1000.
#     1 <= temperatures[i] <= 100
class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        output = [0] * len(temperatures)
        stack = [] # adding warmer and previous colder popping out of the stack
        # we are looping and for each index returning number of index with days that has warmer value
        # stack is used for storing warmer index temperature

        # monotonic decreasing stack
        # goal is to use 2 values in stack as tuple !!!! And popping from stack all values less warmed than the given day temperature
        for index, day in enumerate(temperatures):
            while stack and day > stack[-1][1]:
                index_s, temp = stack.pop()
                output[index_s] = index - index_s

            stack.append((index, day))

        return output