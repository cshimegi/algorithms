# Questions to ask:
# 1. What is the time complexity? O(n)
# 2. What is the space complexity? O(n)
class Solution:
    def pivotArray(self, nums: list[int], pivot: int) -> list[int]:
        smaller, equal, greater = [], [], []
        for num in nums:
            if num < pivot:
                smaller.append(num)
            elif num == pivot:
                equal.append(num)
            else:
                greater.append(num)
        return smaller + equal + greater


# Problem 2161
# Link: https://leetcode.com/problems/partition-array-according-to-given-pivot/description/
if __name__ == '__main__':
    s = Solution()
    cases = [
        ([9,12,5,10,14,3,10], 10),
        ([2,3,5,8,4], 3)
    ]

    for case in cases:
        print(s.pivotArray(case[0], case[1]))