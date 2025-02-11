# Questions to ask:
# 1. What is the time complexity? O(1)
# 2. What is the space complexity?
class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # Hashmap: key -> Node
        # Create dummy head and tail for the doubly linked list
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: Node):
        """Remove a node from the double linked list."""
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _add_to_front(self, node: Node):
        """Add a node to the front (most recently used position) of the list."""
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            # Move the accessed node to the front
            self._remove(node)
            self._add_to_front(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Update the value of the existing node
            node = self.cache[key]
            node.value = value
            # Move it to the front
            self._remove(node)
            self._add_to_front(node)
        else:
            if len(self.cache) == self.capacity:
                # Remove the least recently used node
                lru = self.tail.prev
                self._remove(lru)
                del self.cache[lru.key]
            # Add the new node
            new_node = Node(key, value)
            self.cache[key] = new_node
            self._add_to_front(new_node)


# Problem 146
# Link: https://leetcode.com/problems/lru-cache/description/
# Tips:
if __name__ == '__main__':
    l = LRUCache(2)
    l.put(1, 1)
    l.put(2, 2)
    print(l.get(1))
    l.put(3, 3)
    print(l.get(2))
    l.put(4,4)
    print(l.get(1))
    print(l.get(3))
    print(l.get(4))

