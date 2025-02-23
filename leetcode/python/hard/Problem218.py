# Questions to ask:
# 1. What is the time complexity? O(n*log(n))
# 2. What is the space complexity?
class Solution:
    def getSkyline(self, buildings: list[list[int]]) -> list[list[int]]:
        from collections import Counter

        events = []
        # Step 1: Convert buildings into events
        for l, r, h in buildings:
            events.append((l, h))   # Start event (positive height)
            events.append((r, -h))  # End event (negative height)
    
        # Step 2: Sort events
        events.sort(key=lambda x: (x[0], -x[1]))  # Start before end at same x
    
        # Step 3: Process events with Counter + Sorted List
        active_heights = [0]  # List maintaining active heights, initially ground level
        height_count = Counter({0: 1})  # Tracks height frequencies
        ans = []
        prev_max_h = 0  # Previous max height
    
        for x, h in events:
            if h > 0:  # Start of building
                if height_count[h] == 0:
                    bisect.insort(active_heights, h)  # Insert in sorted order
                height_count[h] += 1  # Increase count
            else:  # End of building
                h = -h  # Convert back to positive
                height_count[h] -= 1  # Decrease count
                if height_count[h] == 0:  # Fully removed
                    active_heights.remove(h)
    
            # Step 4: Get current max height
            curr_max_h = active_heights[-1]  # Get max height safely
    
            # Step 5: If height changed, add to ans
            if curr_max_h != prev_max_h:
                ans.append([x, curr_max_h])
                prev_max_h = curr_max_h
    
        return ans


# Problem 218
# Link: https://leetcode.com/problems/the-skyline-problem/description/
if __name__ == '__main__':
    s = Solution()
    cases = [
        [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]],
        [[0,2,3],[2,5,3]]
    ]
    for case in cases:
        print(s.getSkyline(case))

