class PositiveIDRegistry:
    def __init__(self):
        self.registered_ids = set()
        self.minimum_unused_id = 1  # Tracks the next smallest ID when the heap is empty

    def register_id(self, x: int) -> None:
        """Registers a specific ID if it is not already taken."""
        if x in self.registered_ids:
            return  # ID is already registered

        self.registered_ids.add(x)

        # If x is the smallest unused ID, adjust self.next_id
        if x == self.minimum_unused_id :
            while self.minimum_unused_id  in self.registered_ids:
                self.minimum_unused_id  += 1  # Increment next_id to the next unused value

    def register_minimal_unused_id(self) -> int:
        """Finds and registers the smallest unused ID."""
        min_id = self.minimum_unused_id
        self.registered_ids.add(min_id)

        while self.minimum_unused_id in self.registered_ids:
            self.minimum_unused_id += 1

        return min_id


if __name__ == "__main__":
    registry = PositiveIDRegistry()
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