# Questions to ask:
# 1. What is the time complexity? O(n*log(m))
# 2. What is the space complexity? O(1)

# BINARY SEARCH PATTERNS: When to use +1 in mid calculation
#
# There are TWO main binary search patterns:
#
# 1. RIGHT BOUNDARY SEARCH (use +1):
#    - Goal: Find the LARGEST value that satisfies condition
#    - Pattern: mid = (l + r + 1) // 2
#    - Update: if check(mid): l = mid; else: r = mid - 1
#    - Why +1? Prevents infinite loop when l = r - 1
#
# 2. LEFT BOUNDARY SEARCH (no +1):
#    - Goal: Find the SMALLEST value that satisfies condition  
#    - Pattern: mid = (l + r) // 2
#    - Update: if check(mid): l = mid + 1; else: r = mid
#    - Why no +1? Natural progress when l = r - 1
#
# INFINITE LOOP PREVENTION:
# - RIGHT BOUNDARY: Without +1, when l=r-1: mid = (r-1+r)//2 = r-1
#   Then l = mid = r-1, creating infinite loop
# - LEFT BOUNDARY: Without +1, when l=r-1: mid = (r-1+r)//2 = r-1  
#   Then l = mid+1 = r, making progress
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
            # WHY +1 HERE? This is the RIGHT BOUNDARY search pattern
            # We use +1 to avoid infinite loop when l = r - 1
            # Without +1: mid = (l + r) // 2 = (r-1 + r) // 2 = (2r-1) // 2 = r-1
            # With +1: mid = (l + r + 1) // 2 = (r-1 + r + 1) // 2 = (2r) // 2 = r
            mid = (l + r + 1) // 2
            if check(mid):
                l = mid  # Keep mid as potential answer
            else:
                r = mid - 1  # Exclude mid from search space
        return l

    def maximumCandies2(self, candies: List[int], k: int) -> int:
        # ALTERNATIVE: LEFT BOUNDARY search pattern (without +1)
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

        l, r = 1, total_candies // k
        while l < r:
            # NO +1 HERE: This is the LEFT BOUNDARY search pattern
            # mid = (l + r) // 2
            # When l = r - 1: mid = (r-1 + r) // 2 = (2r-1) // 2 = r-1
            # This ensures progress: l = mid + 1 = (r-1) + 1 = r
            mid = (l + r) // 2
            if check(mid):
                l = mid + 1  # Exclude mid from search space
            else:
                r = mid  # Keep mid as potential answer
        if check(l):
            return l
        else:
            return l - 1

# Problem 2226
# Link: https://leetcode.com/problems/maximum-candies-allocated-to-k-children/description/
if __name__ == '__main__':
    s = Solution()
    cases = [
        ([5, 8, 6], 3, 5),
        ([2, 5], 11, 0),
        ([5, 8, 6, 8], 3, 6),
        ([5, 8, 6, 8], 4, 5),
        ([5, 8, 6, 8], 5, 4),
        ([5, 8, 20], 3, 8)
    ]
    for candies, k, expected in cases:
        assert s.maximumCandies(candies, k) == expected
