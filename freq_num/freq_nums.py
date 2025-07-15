class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # find the most frequent elements in the array
        # find one or three
        most_frequent = {}
        for item in nums:
            if item not in most_frequent:
                most_frequent[item] = 1
            else:
                most_frequent[item] += 1

        bucket = [[] for _ in range(len(nums) + 1)]

        # have to use key otherwise it rewrite k or target as input parameter in func
        for (key, v) in most_frequent.items():
            bucket[v].append(key)

        # bucket = [
        #     [],        # index 0 (not used)
        #     [1],       # freq 1
        #     [2],       # freq 2
        #     [3],       # freq 3
        #     [], [], [] # freq 4-6 (empty)
        # ]
        result = []
        for freq in range(len(bucket) - 1, 0, -1):
            for num in bucket[freq]:
                result.append(num)
            l = len(result)
            if l == k:
                break

        return result



if __name__ == "__main__":
    nums = [1, 2, 2, 3, 3, 3]
    k = 2
    print("Result is:")
    print(Solution().topKFrequent(nums, k))