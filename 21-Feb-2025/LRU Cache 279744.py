# Problem: LRU Cache - https://leetcode.com/problems/lru-cache/

class Node:
    def __init__(self, key):
        self.val = key
        self.prev = None
        self.next = None
        
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.elements = {}
        self.nodes = {}
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.elements:
            return -1
        node = self.nodes[key]
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node
        return self.elements[key]

    def put(self, key: int, value: int) -> None:
        if key in self.elements:
            self.elements[key] = value
            node = self.nodes[key]
            node.prev.next = node.next
            node.next.prev = node.prev
        else:
            if len(self.elements) == self.capacity:
                lru = self.head.next
                self.head.next = lru.next
                lru.next.prev = self.head
                del self.elements[lru.val]
                del self.nodes[lru.val]
            self.elements[key] = value
            node = Node(key)
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node
        self.nodes[key] = node
