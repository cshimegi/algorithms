# Questions to ask:
# 1. What is the time complexity?
# 2. What is the space complexity?
class SnapshotArray:
    def __init__(self, length: int):
        self.storage = {}
        self.snapshots = []
        self.updated = True

    def set(self, index: int, val: int) -> None:
        self.storage[index] = val
        self.updated = True

    def snap(self) -> int:
        if self.updated:
            self.snapshots.append({**self.storage})
            self.updated = False
        else:
            self.snapshots.append(self.snapshots[-1])
        return len(self.snapshots)-1

    def get(self, index: int, snap_id: int) -> int:
        return self.snapshots[snap_id].get(index, 0)

class SnapshotArray2:
    """
    Optimized space complexity
    """
    def __init__(self, length: int):
        # Space complexity: O(n)
        self.snaps = {i: [(0, 0)] for i in range(length)}
        self.snap_id = 0

    def set(self, index: int, val: int) -> None:
        if self.snaps[index][-1][0] == self.snap_id:
            self.snaps[index][-1] = (self.snap_id, val)  # Overwrite last value in current snap
        else:
            self.snaps[index].append((self.snap_id, val))  # Store new value

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        # O(log(n)) n is size of self.snaps
        snaps = self.snaps[index]
        left, right = 0, len(snaps) - 1
        while left <= right:  # Binary search for the latest snapshot ≤ snap_id
            mid = (left + right) // 2
            if snaps[mid][0] <= snap_id:
                left = mid + 1
            else:
                right = mid - 1
        return snaps[right][1]

# Problem 1146
# Link: https://leetcode.com/problems/snapshot-array/description/
if __name__ == '__main__':
    s = SnapshotArray()
