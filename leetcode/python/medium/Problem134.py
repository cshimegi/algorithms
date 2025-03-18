# Questions to ask:
# 1. What is the time complexity? O(n)
# 2. What is the space complexity? O(1)
from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_surplus = 0
        curr_surplus = 0
        start_idx = 0

        for i in range(len(gas)):
            surplus = gas[i] - cost[i]
            total_surplus += surplus
            curr_surplus += surplus

            if curr_surplus < 0:
                start_idx = i+1
                curr_surplus = 0

        return start_idx if total_surplus >= 0 else -1

# Problem 134
# Link: https://leetcode.com/problems/gas-station/description/
# Tips:
if __name__ == '__main__':
    s = Solution()
    cases = [
        ([1,2,3,4,5], [3,4,5,1,2], 3),
        ([2,3,4], [3,4,3], -1)
    ]
    for gas, cost, expected in cases:
        assert s.canCompleteCircuit(gas, cost) == expected
