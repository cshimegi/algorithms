# Questions to ask:
# 1. What is the time complexity? O(n*log(max(ranks) * cars^2))
# 2. What is the space complexity? O(1)
import math
from typing import List

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def check(guess_time: int) -> bool:
            cars_repaired = 0
            for rank in ranks:
                cars_repaired += int(math.sqrt(guess_time / rank))
                if cars_repaired >= cars:
                    return True
            return False

        # min and max time to repair all cars
        left, right = 1, max(ranks) * cars * cars
        while left < right:
            mid = (left+right) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1
        return left


# Problem 2594
# Link: https://leetcode.com/problems/minimum-time-to-repair-cars/description/
if __name__ == '__main__':
    s = Solution()
    cases = [
        ([4, 2, 3, 1], 10),
        ([5, 1, 8], 6),
        ([1,1,3,3], 74)
    ]
    for ranks, cars in cases:
        print(s.repairCars(ranks, cars))
