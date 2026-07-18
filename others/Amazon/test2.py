# Questions to ask:
# 1. What is the time complexity?
# 2. What is the space complexity?
class Solution:
    def calculatePendingOrders(self, orderProcessingTime: list[int], shiftDurations: list[int]) -> list[int]:
        from bisect import bisect_right

        n = len(orderProcessingTime)
        prefix_sum = [0] * n
        prefix_sum[0] = orderProcessingTime[0]

        for i in range(1, n):
            prefix_sum[i] = prefix_sum[i-1] + orderProcessingTime[i]

        total_order_time = prefix_sum[-1]
        tsd = 0
        result = []
        print("prefix_sum ==> ", prefix_sum)
        for duration in shiftDurations:
            tsd += duration

            idx = bisect_right(prefix_sum, tsd)
            pending = n - idx
            result.append(pending)
            if tsd >= total_order_time:
                tsd = 0

        return result




# Problem Amazon2
# Link: https://leetcode.com/discuss/post/6460397/amazon-sde-ii-oa-by-user2979x-btnz/
if __name__ == '__main__':
    # 1 <= n, m <= 2*10^5
    # 1 <= orderProcessTime[i], shiftDurations[i] <= 10^9
    s = Solution()
    cases = [
        [
            [2,4,5,1,1], [1,5,1,5,2] # [5,3,3,1,0]
        ],
        [
            [1,2,4,1,2], [3,10,1,1,1] # [3,0,4,4,3]
        ],
        [
            [1,4,4], [9,1,4] # [0,2,1]
        ]
    ]

    for case in cases:
        print(s.calculatePendingOrders(case[0], case[1]))
