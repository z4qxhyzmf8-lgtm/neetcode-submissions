class Node:

    def __init__(self, key, val):
        self.val = val
        self.key = key
        self.next = None
        self.prev = None 

class LRUCache:

    def __init__(self, capacity: int):
        self.size = capacity
        self.dict = {} #maps key to node
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        next_node = node.next
        prev_node = node.prev
        prev_node.next = next_node
        next_node.prev = prev_node
    
    def insert(self, node):
        prev_node = self.right.prev
        next_node = self.right
        prev_node.next = node
        next_node.prev = node
        node.next = next_node
        node.prev = prev_node

    def get(self, key: int) -> int:
        if key in self.dict:
            self.remove(self.dict[key])
            self.insert(self.dict[key])
            return self.dict[key].val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            self.remove(self.dict[key])
        self.dict[key] = Node(key, value)
        self.insert(self.dict[key])
        if len(self.dict) > self.size:
            LRU = self.left.next
            self.remove(LRU)
            del self.dict[LRU.key]

        
        
