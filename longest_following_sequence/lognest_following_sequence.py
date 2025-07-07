from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_map = set(nums)
        longest = 0
        for num in nums:
            # find a start by checking left neighbour of current elem in HashMap, that it take O(n)
            if num - 1 not in hash_map:
                length = 1
                while num + length in hash_map:
                    length += 1

                longest = max(longest, length)

        return longest


if __name__ == '__main__':
    solution = Solution()
    res = solution.longestConsecutive(nums=[2, 20, 4, 10, 3, 4, 5])
    if res == 4:
        print("Test passed")
    else:
        print("Test failed")
