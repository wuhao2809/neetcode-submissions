class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None
        
class LRUCache:

    def __init__(self, capacity: int):
        # dll
        self.root = Node()
        self.tail = None
        self.hashmap = {}
        self.capacity = capacity
        

    def get(self, key: int) -> int:
        if key in self.hashmap:
            self.remove(self.hashmap[key])
            self.addFront(self.hashmap[key])
            return self.hashmap[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        # add
        if key in self.hashmap:
            self.hashmap[key].val = value
            self.remove(self.hashmap[key])
            self.addFront(self.hashmap[key])
        else:
            curr = Node(key, value)
            self.hashmap[key] = curr
            self.addFront(curr)

            if len(self.hashmap) > self.capacity:
                lru = self.tail
                self.remove(lru)
                del self.hashmap[lru.key]
        
        # remove redundant
    def addFront(self, node):
        prev_first = self.root.next
        self.root.next = node
        node.prev = self.root

        node.next = prev_first
        if prev_first:
            prev_first.prev = node
        else:
            self.tail = node
        return
    
    def remove(self, node):
        prev = node.prev
        nxt = node.next

        prev.next = nxt
        if nxt:
            nxt.prev = prev
        else:
            self.tail = prev
        return
        
        
