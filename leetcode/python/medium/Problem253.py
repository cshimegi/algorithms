# Questions to ask:
# 1. What is the time complexity? O(n*log(n))
# 2. What is the space complexity? O(n)
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    def minMeetingRooms(self, intervals: list[Interval]) -> int:
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        ans, count = 0, 0
        i, j = 0, 0
        while i < len(intervals):
            if start[i] < end[j]:
                i += 1
                count += 1
            else:
                j += 1
                count -= 1
            ans = max(ans, count)
        return ans

    def minMeetingRooms2(self, intervals: list[Interval]) -> int:
        events = []

        for i in intervals:
            events.append((i.start, 1))  # Room required
            events.append((i.end, -1))   # Room freed

        # Sort by time; in case of tie, end (-1) comes before start (+1)
        events.sort()

        max_rooms, curr_rooms = 0, 0
        for _, event in events:
            curr_rooms += event
            max_rooms = max(max_rooms, curr_rooms)

        return max_rooms


# Problem 253
# Link: https://leetcode.com/problems/meeting-rooms-ii/description/
# https://memorylimitexceeded.gitlab.io/leetcode/problems/0253-meeting-rooms-ii.html
if __name__ == '__main__':
    s = Solution()
    cases = [
        [Interval(0, 30), Interval(5, 10), Interval(15, 20)], # 2
        [Interval(7, 10), Interval(2, 4)], # 1
        [
            Interval(13, 15),
            Interval(2, 5),
            Interval(8, 12),
            Interval(4, 8),
            Interval(6, 9)] # 2
    ]
    for case in cases:
        print(s.minMeetingRooms(case))
        print(s.minMeetingRooms2(case))

