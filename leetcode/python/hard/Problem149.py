# Questions to ask:
# 1. What is the time complexity?
# 2. What is the space complexity?
class Solution:
    def maxPoints(self, points: list[list[int]]) -> int:
        from collections import defaultdict
        from math import gcd

        n = len(points)
        if n <= 2:
            return n

        max_count = 0
    
        for i in range(n):
            slopes = defaultdict(int)
            same_point = 0
            vertical = 0
            local_max = 0
            x1, y1 = points[i]
    
            for j in range(n):
                if i == j:
                    continue
                x2, y2 = points[j]
    
                if x1 == x2 and y1 == y2:
                    same_point += 1
                elif x1 == x2:
                    vertical += 1
                else:
                    dy, dx = y2 - y1, x2 - x1
                    g = gcd(dy, dx)
                    slope = (dy // g, dx // g)  # Normalize slope
                    slopes[slope] += 1
                    local_max = max(local_max, slopes[slope])
    
            max_count = max(max_count, max(local_max, vertical) + same_point + 1)
    
        return max_count


# Problem 149
# Link: https://leetcode.com/problems/max-points-on-a-line/description/
if __name__ == '__main__':
    s = Solution()
    cases = [
        [[1,1],[2,2],[3,3]],
        [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
    ]
    for case in cases:
        print(s.maxPoints(case))

