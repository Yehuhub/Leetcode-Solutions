# Main trick here is to create dummy head and dummy tail, that way we have a lot less edge cases
# we save a map that way we can find nodes in O(1), than adding, moving and removing is in O(1)
# since its a linked list

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = dict()

        self.dummy_head = Node(0,0)
        self.dummy_tail = Node(0,0)

        self.dummy_head.next = self.dummy_tail
        self.dummy_tail.prev = self.dummy_head


    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        
        node = self.map[key]
        self.remove(node)
        self.insert(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.remove(self.map[key])

        node = Node(key, value)
        self.insert(node)
        self.map[key] = node
        if len(self.map) > self.capacity:
            last_node = self.dummy_tail.prev
            self.remove(last_node)
            self.map.pop(last_node.key)

        
    def remove(self, node):
        prev = node.prev
        nxt = node.next

        prev.next = nxt
        nxt.prev = prev

    def insert(self, node):
        node.next = self.dummy_head.next
        node.prev = self.dummy_head

        self.dummy_head.next.prev = node
        self.dummy_head.next = node

