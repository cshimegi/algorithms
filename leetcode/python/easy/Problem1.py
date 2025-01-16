class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        records = {}
        for idx, num in enumerate(nums):
            r = target - num
            if r in records:
                # Since it's guaranteed that there is only one solution
                return [records[r], idx]
            records[num] = idx


# Problem 1
# Link: https://leetcode.com/problems/two-sum/description/
if __name__ == '__main__':
    s = Solution()
    print(s.twoSum(nums = [2,7,11,15], target = 9))
    print(s.twoSum(nums = [3,2,4], target = 6))
