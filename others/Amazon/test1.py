# Questions to ask:
# 1. What is the time complexity?
# 2. What is the space complexity?
#
class Solution:
    def findOptimalPermutation(self, nums: list[int]) -> list[int]:
        # Find the lexicographically smallest permutation of idx + 1 with max gain
        # Example: [2,1,2], index array = [0,1,2], idx+1 permutation [2,1,3] => max gain = 1*1 + 2*2 + 3*2 = 11
        # Example: [2,1,2,3], index array = [0,1,2,3], idx+1 permutation [2,1,3,4] => max gain = 1*1 + 2*2 + 3*2 + 4*3 = 23
        # Example: [5,6,1,4,4], index array = [0,1,2,3,4], idx+1 permutation [3,4,5,1,2] => max gain = 1*1 + 2*4 + 3*4 + 4*5 + 5*6 = 71

        n = len(nums)
        max_gain = 0
        max_gain_permutations = []

        def calculate_gain(permutation):
            gain = 0
            for i, val in enumerate(permutation):
                gain += (i + 1) * nums[val - 1]
            return gain

        def backtrack(current_permutation, available_indices):
            nonlocal max_gain, max_gain_permutations
            if len(current_permutation) == n:
                gain = calculate_gain(current_permutation)
                if gain > max_gain:
                    max_gain = gain
                    max_gain_permutations = [current_permutation[:]]
                elif gain == max_gain:
                    max_gain_permutations.append(current_permutation[:])
                return

            for i in range(len(available_indices)):
                next_index = available_indices[i]
                backtrack(current_permutation + [next_index], available_indices[:i] + available_indices[i + 1:])

        backtrack([], list(range(1, n + 1)))

        if not max_gain_permutations:
            return []

        return min(max_gain_permutations)

    def findOptimalPermutation2(self, nums: list[int]) -> list[int]:
        n = len(nums)
        indexed_nums = [(nums[i], i + 1) for i in range(n)]
        indexed_nums.sort()

        permutations = [index for value, index in indexed_nums]
        return permutations


# Problem Amazon1
# Link: https://leetcode.com/discuss/post/6307796/amazon-sde-2-online-assessment-question-bukvi/
if __name__ == '__main__':
    # 1 <= n <= 10^5
    # 1 <= nums[i] <= 10^9
    s = Solution()
    cases = [
        [2,1,2], # idx+1 permutation [2,1,3] => max gain = 1*1 + 2*2 + 3*2 = 11
        [2,1,2,3], # idx+1 permutation [2,1,3,4] => max gain = 1*1 + 2*2 + 3*2 + 4*3 = 23
        [5,6,1,4,4], # idx+1 permutation [3,4,5,1,2] => max gain = 1*1 + 2*4 + 3*4 + 4*5 + 5*6 = 71
        []
    ]

    for case in cases:
        print(s.findOptimalPermutation2(case))
