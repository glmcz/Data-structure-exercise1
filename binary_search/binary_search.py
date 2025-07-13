import math


class Solution:
    def binary_search(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            # (l + r) // 2 can lead to overflow
            m = l + ((r - l) // 2)
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return nums[m]
        return -1


    def binary_recursive_helper(self, l, r , nums: list[int], target: int) -> int:
        if l > r:
            return -1
        mid = l + ((r -l) // 2)
        if nums[mid] == target:
            return nums[mid]
        elif nums[mid] < target:
            return self.binary_recursive_helper(mid + 1, r, nums, target)
        return self.binary_recursive_helper(l, mid -1, nums, target)


    def binary_recursive(self, nums: list[int], target: int) -> int:
        return self.binary_recursive_helper(0, len(nums)-1, nums, target)



    def binary_search_ol(self, nums:list[int], target) -> int:
        # works only if input is sorted desc
        if target >= len(nums):
            pivot = math.floor(len(nums))
        elif target <= len(nums):
            pivot = math.floor(len(nums) / 2)
        else:
            pivot = nums[target]
            if pivot == target:
                return pivot

        target = abs(target)
        sub_filed = nums
        while pivot != target:
            if pivot <= target:
                print("search on left")
                new_pivot_index = int(len(sub_filed) / 2)
                new_pivot = sub_filed[new_pivot_index]
                sub_filed = sub_filed[:new_pivot_index]
                if len(sub_filed) == 1:
                    return 0

                pivot = new_pivot
            elif pivot >= target:
                new_pivot_index = int(len(sub_filed) / 2)
                new_pivot = sub_filed[new_pivot_index]
                if len(sub_filed) == 1:
                    return 0
                sub_filed = sub_filed[new_pivot_index:]
                pivot = new_pivot
                print("search on right")

        return pivot


if __name__ == "__main__":
    target = 7
    nums = [-1, 1, 2, 4, 5, 6, 7]
    print(f"  Solution of binary search for target {target} is {Solution().binary_recursive(nums, target=target)}")
