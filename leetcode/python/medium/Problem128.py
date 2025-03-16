# Questions to ask:
# 1. What is the time complexity? O(n)
# 2. What is the space complexity? O(n)
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums:
            return 0

        num_set = set(nums) # sorted: [100,4,200,1,3,2] -> {1, 2, 3, 100, 4, 200}
        ans = 0

        for n in num_set:
            # Only start a sequence if `n` is the beginning of a sequence
            if n - 1 not in num_set:
                current_num = n
                count = 1

                # Check for the next numbers in the sequence
                while current_num + 1 in num_set:
                    current_num += 1
                    count += 1

                ans = max(ans, count)

        return ans

# Problem 128
# Link: https://leetcode.com/problems/longest-consecutive-sequence/description/
# Tips:
if __name__ == '__main__':
    s = Solution()