class Storage:
    """
    Optimized space complexity
    """
    def __init__(self):
        # Space complexity: O(n)
        # self.snaps = {i: [(0, 0)] for i in range(length)}
        self.snaps = {}
        self.snap_ver = 1

    def set(self, key: int, val: int) -> None:
        if not key in self.snaps:
            self.snaps[key] = [(self.snap_ver, val)]
        elif self.snaps[key][-1][0] == self.snap_ver:
            self.snaps[key][-1] = (self.snap_ver, val)  # Overwrite last value in current snap
        else:
            self.snaps[key].append((self.snap_ver, val))  # Store new value

    def snap(self) -> int:
        self.snap_ver += 1
        return self.snap_ver - 1

    def get(self, key: int, snap_ver: int) -> int | None:
        # O(log(n)) n is size of self.snaps
        if key not in self.snaps:
            return None

        snaps = self.snaps[key]
        left, right = 0, len(snaps) - 1
        while left <= right:  # Binary search for the latest snapshot ≤ snap_ver
            mid = (left + right) // 2
            if snaps[mid][0] <= snap_ver:
                left = mid + 1
            else:
                right = mid - 1

        if snaps[right][0] != snap_ver:
            return None

        return snaps[right][1]

    def get2(self, key: int, snap_ver: int) -> int | None:
        # O(log(n)) n is size of self.snaps
        if key not in self.snaps:
            return None

        snaps = self.snaps[key]
        left, right = 0, len(snaps) - 1
        while left <= right:  # Binary search for the latest snapshot ≤ snap_ver
            mid = (left + right) // 2
            if snaps[mid][0] <= snap_ver:
                left = mid + 1
            else:
                right = mid - 1

        if snaps[left-1][0] != snap_ver:
            return None

        return snaps[left-1][1]

    @property
    def get_all_snaps(self):
        return self.snaps

if __name__ == "__main__":
    storage = Storage()
    storage.set(1, 5)
    storage.set(1, 6)
    print("(key, ver)1 = (1, 1)", storage.get(1, 1))
    print("(key, ver)2 = (1, 1)", storage.get2(1, 1))
    print("(key, ver)1 = (1, 2)", storage.get(1, 2))
    print("(key, ver)2 = (1, 2)", storage.get2(1, 2))
    storage.snap() # ---> ver = 1
    storage.set(1, 3)
    print("(key, ver)1 = (1, 1)", storage.get(1, 1))
    print("(key, ver)2 = (1, 1)", storage.get2(1, 1))
    print("(key, ver)1 = (2, 2)", storage.get(2, 2))
    print("(key, ver)2 = (2, 2)", storage.get2(2, 2))
    storage.snap() # ---> ver = 2
    print("(key, ver)1 = (2, 1)", storage.get(2, 1))
    print("(key, ver)2 = (2, 1)", storage.get2(2, 1))
    print("(key, ver)1 = (1, 2)", storage.get(1, 2))
    print("(key, ver)2 = (1, 2)", storage.get2(1, 2))
    storage.snap() # ---> ver = 3
    storage.snap() # ---> ver = 4
    storage.snap() # ---> ver = 5
    print("(key, ver)1 = (1, 5)", storage.get(1, 5))
    print("(key, ver)2 = (1, 5)", storage.get2(1, 5))
    print(storage.get_all_snaps)
    print("(key, ver)1 = (1, 1)", storage.get(1, 1))
    print("(key, ver)2 = (1, 1)", storage.get2(1, 1))