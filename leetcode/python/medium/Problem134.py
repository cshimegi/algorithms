# Questions to ask:
# 1. What is the time complexity?
# 2. What is the space complexity?
class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
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
    print(s.canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2]))