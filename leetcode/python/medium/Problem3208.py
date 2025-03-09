# Questions to ask:
# 1. What is the time complexity?
# 2. What is the space complexity?
from typing import List

class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        # Time Limit Exceeded
        # O(n^2)/ O(1)
        colors.extend(colors[:k])
        ans = 0
        i = 0
        while i < len(colors) - k:
            if colors[i] != colors[i+1]:
                j = i
                while j < i+k-1:
                    if colors[j] == colors[j+1]:
                        break
                    j += 1
                if j == i+k-1:
                    ans += 1
            i += 1

        return ans


    def numberOfAlternatingGroups2(self, colors: List[int], k: int) -> int:
        # Sliding Window
        # O(n)/ O(1)
        colors.extend(colors[:k-1])
        n = len(colors)
        ans = 0
        left = 0  # Start of window

        for right in range(1, n):
            # If the alternating pattern breaks, reset left pointer
            if colors[right] == colors[right - 1]:
                left = right

            # If window size reaches `k`, count it
            if right - left + 1 >= k:
                ans += 1

        return ans


# Problem 3208
# Link: https://leetcode.com/problems/alternating-groups-ii/description/
if __name__ == '__main__':
    s = Solution()
    cases = [
        ([0, 1, 0, 1, 0], 3),
        ([0, 1, 0, 0, 1, 0, 1], 6),
        ([1, 1, 0, 1], 4),
        ([1, 1, 1, 1], 3),
        ([0, 1, 0, 1, 0, 1, 0, 1, 0, 1], 4),
    ]
    for colors, k in cases:
        print(s.numberOfAlternatingGroups(colors, k))

