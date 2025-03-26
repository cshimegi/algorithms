# Questions to ask:
# 1. What is the time complexity? O(n*log(n))
# 2. What is the space complexity? O(1)
class Solution:
    def checkValidCuts(self, n: int, rectangles: list[list[int]]) -> bool:
        total = len(rectangles)

        def check(intervals: list[list[int]], sort_axis: int) -> bool:
            intervals.sort(key=lambda x: x[sort_axis])
            sections = 0
            max_end = intervals[0][sort_axis + 2]
            for i in range(total):
                start, end = intervals[i][sort_axis], intervals[i][sort_axis + 2]
                if max_end <= start:
                    sections += 1
                    if sections == 2:
                        return True
                max_end = max(max_end, end)
            return False

        return check(rectangles, 0) or check(rectangles, 1)


# Problem 3394
# Link: https://leetcode.com/problems/check-if-grid-can-be-cut-into-sections/description/
if __name__ == '__main__':
    s = Solution()
    cases = [
        (5, [[1, 0, 5, 2], [0, 2, 2, 4], [3, 2, 5, 3], [0, 4, 4, 5]], True),
        (4, [[0, 0, 1, 1], [2, 0, 3, 4], [0, 2, 2, 3], [3, 0, 4, 3]], True),
        (4, [[0, 2, 2, 4], [1, 0, 3, 2], [2, 2, 3, 4], [3, 0, 4, 2], [3, 2, 4, 4]], False),
    ]
    for n, rectangles, expected in cases:
        assert s.checkValidCuts(n, rectangles) == expected
