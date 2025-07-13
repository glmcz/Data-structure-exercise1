# Minimum Stack
# Solved
#
# Design a stack class that supports the push, pop, top, and getMin operations.
#
#     MinStack() initializes the stack object.
#     void push(int val) pushes the element val onto the stack.
#     void pop() removes the element on the top of the stack.
#     int top() gets the top element of the stack.
#     int getMin() retrieves the minimum element in the stack.
#
# Each function should run in O(1)O(1) time.


class Solution:
    def __init__(self):
        self.stack = []
        self.min_stack = []


    def push(self, value):
        self.stack.append(value)
        val = min(value, self.min_stack[-1] if self.min_stack else value)
        self.min_stack.append(val)

    def top(self)-> int:
        return self.stack[-1]

    def pop(self):
        self.stack.pop()

    # get actual minimum not global minimum from all values in stack
    def get_min(self):
        return self.min_stack[-1]
        