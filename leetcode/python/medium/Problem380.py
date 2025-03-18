# Questions to ask:
# 1. What is the time complexity? O(1)
# 2. What is the space complexity?
import random

class RandomizedSet:
    def __init__(self):
        self.num_to_idx = {}  # Stores value → index mapping
        self.values = []  # Stores actual values

    def insert(self, val: int) -> bool:
        if val in self.num_to_idx:
            return False  # Already exists

        self.num_to_idx[val] = len(self.values)  # Store index
        self.values.append(val)  # Append to list
        return True

    def remove(self, val: int) -> bool:
        if val not in self.num_to_idx:
            return False  # Not found

        # Swap the element with the last element
        last_val = self.values[-1]
        idx = self.num_to_idx[val]
        self.values[idx] = last_val
        self.num_to_idx[last_val] = idx

        # Remove last element
        self.values.pop()
        del self.num_to_idx[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.values)


# Problem 380
# Link: https://leetcode.com/problems/insert-delete-getrandom-o1/description/
# Tips:
if __name__ == '__main__':
    r = RandomizedSet()

