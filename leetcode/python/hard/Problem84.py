# Questions to ask:
# 1. What is the time complexity?
# 2. What is the space complexity?
class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        stack = []  # stores indices
        max_area = 0
        heights.append(0)  # Sentinel to force stack emptying at the end

        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]  # Pop height
                width = i if not stack else i - stack[-1] - 1  # Compute width
                max_area = max(max_area, height * width)

            stack.append(i)  # Push current index

        return max_area


    def largestRectangleArea2(self, heights: list[int]) -> int:
        # Reference: https://www.youtube.com/watch?v=zx5Sw9130L0
        stack = []  # stores pairs (index,height)
        max_area = 0

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                max_area = max(max_area, height * (i - index))
                start = index

            # Store the backtracked start index with current height
            stack.append((start, h))

        # Process the remaining
        for i, h in stack:
            max_area = max(max_area, h * (len(height) - i))

        return max_area

    def largestRectangleArea3(self, heights: List[int]) -> int:
        stack = []  # Stores pairs (index, height)
        max_area = 0

        # Sentinel to forcefully process all remaining bars
        heights.append(0)

        for i, h in enumerate(heights):
            start = i  # Default start index for new heights

            # Pop elements when the current height is smaller (maintaining monotonic stack)
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                max_area = max(max_area, height * (i - index))
                start = index  # Update start to previous index for the popped height

            # Store the backtracked start index with current height
            stack.append((start, h))

        return max_area


# Problem 84
# Link: https://leetcode.com/problems/largest-rectangle-in-histogram/description/
if __name__ == '__main__':
    s = Solution()
    print(s.largestRectangleArea([2,3,4,4]))
    print(s.largestRectangleArea([2,1,5,0,2,3]))
    print(s.largestRectangleArea([2,1,5,6,2,3]))
    print(s.largestRectangleArea([1,1,1,2,2,1,1,1,5]))

