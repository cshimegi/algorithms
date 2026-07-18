# Questions to ask:
# 1. What is the time complexity? O(log(n))
# 2. What is the space complexity? O(n)
from sortedcontainers import SortedSet

class PositiveIDRegistry:
    def __init__(self):
        self.registered = set()  # Keeps track of registered IDs
        self.available = SortedSet([1])  # Keeps track of available IDs

    def register_id(self, x: int) -> None: # O(log(n))
        if x in self.registered:
            return
        self.registered.add(x)  # O(log(n))

        # If x was previously available, remove it from available IDs
        if x in self.available:
            self.available.remove(x) # O(log(n))

        # Add the next possible unused ID
        next_id = x + 1
        if next_id not in self.registered:
            self.available.add(next_id)  # O(log(n))

    def register_minimal_unused_id(self) -> int: # O(log(n))
        min_id = self.available.pop(0)  # Get and remove the smallest unused ID
        self.registered.add(min_id)

        # Add the next possible unused ID if not already registered
        next_id = min_id + 1
        if next_id not in self.registered:
            self.available.add(next_id)

        return min_id


if __name__ == "__main__":
    registry = PositiveIDRegistry()

    # Register all numbers except 4
    for i in range(1, 10**3 + 1):
        if i not in {4, 23, 49, 50, 51, 100}:
            registry.register_id(i)

    registry.register_id(3)
    print(registry.register_minimal_unused_id())
    print(registry.register_minimal_unused_id())
    print(registry.register_minimal_unused_id())
    registry.register_id(1002)
    registry.register_id(1004)
    print(registry.register_minimal_unused_id())
    print(registry.register_minimal_unused_id())
    print(registry.register_minimal_unused_id())
    print(registry.register_minimal_unused_id())
