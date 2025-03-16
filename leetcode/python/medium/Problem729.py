# Questions to ask:
# 1. What is the time complexity? O(log*(n))
# 2. What is the space complexity?
import bisect
class MyCalendar:

    def __init__(self):
        self.calendar = []

    def book(self, startTime: int, endTime: int) -> bool:
        idx = bisect.bisect_left(self.calendar, (startTime, endTime)) # O(log*(n))

        # Check for overlaps
        if idx > 0 and self.calendar[idx - 1][1] > startTime:
            return False  # Overlap with previous event
        if idx < len(self.calendar) and endTime > self.calendar[idx][0]:
            return False  # Overlap with next event

        # No overlap, insert the event
        bisect.insort_left(self.calendar, (startTime, endTime)) # O(log*(n))
        return True



# Problem 937
# Link: https://leetcode.com/problems/my-calendar-i/description/
if __name__ == '__main__':
    mc = MyCalendar()
    books = [
        ([47, 50], True),
        ([33, 41], True),
        ([39, 45], False),
        ([33, 42], False),
        ([25, 32], True),
        ([26, 35], False),
        ([19, 25], True),
        ([3, 8], True),
        ([8, 13], True),
        ([18, 27], False)
    ]
    for book, expected in books:
        print(mc.book(book[0], book[1]) == expected)