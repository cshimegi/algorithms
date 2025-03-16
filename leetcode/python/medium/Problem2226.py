# Questions to ask:
# 1. What is the time complexity? O(n*log(m))
# 2. What is the space complexity? O(1)
from typing import List

class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def check(get_candies: int) -> bool:
            num_of_children = k
            for candy in candies:
                num_of_children -= candy // get_candies
                if num_of_children <= 0:
                    return True
            return False

        total_candies = sum(candies)
        if total_candies < k:
            return 0

        # l = minimum get_candies
        # r = maximum get_candies
        l, r = 1, total_candies // k
        while l < r:
            mid = (l + r + 1) // 2
            if check(mid):
                l = mid
            else:
                r = mid - 1
        return l

# Problem 2226
# Link: https://leetcode.com/problems/maximum-candies-allocated-to-k-children/description/
if __name__ == '__main__':
    s = Solution()
    cases = [
        ([5, 8, 6], 3),
        ([2, 5], 11),
        ([5, 8, 6, 8], 3),
        ([5, 8, 6, 8], 4),
        ([5, 8, 6, 8], 5),
        ([5, 8, 20], 3)
    ]
    for candies, k in cases:
        print(s.maximumCandies(candies, k))

