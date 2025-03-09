# Questions to ask:
# 1. What is the time complexity? O(n)
# 2. What is the space complexity? O(1)
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l, curr_op, min_op = len(blocks), 0, float('inf')
        left, right = 0, 0
        while right < l:
            if blocks[right] == 'W':
                curr_op += 1

            if right - left + 1 == k:
                min_op = min(min_op, curr_op)
                if blocks[left] == 'W':
                    curr_op -= 1
                left += 1

            right += 1
        return min_op

# Problem 2379
# Tips:
# Link: https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/description/
if __name__ == '__main__':
    s = Solution()
    cases = [
        ("WBBWWBBWBW", 7),
        ("WBWBBBW", 2),
        ("BWWWBB", 6)
    ]
    for blocks, k in cases:
        print(s.minimumRecolors(blocks, k))

