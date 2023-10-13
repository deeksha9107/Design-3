# Problem 2: LRU Cache(https://leetcode.com/problems/lru-cache/)
# // Time Complexity : put - O(1), get-O(1)
# // Space Complexity : O(n)
# // Did this code successfully run on Leetcode : Yes
# // Any problem you faced while coding this : No

# Making a class of Nodes
class Listnode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.head = None
        self.tail = None


class LRUCache:
    def __init__(self, capacity: int):
        # making capacity global
        self.capacity = capacity
        # hashmap for cache
        self.cache = {}
        # initializing head and tail
        self.head = Listnode(-1, -1)
        self.tail = Listnode(-1, -1)
        # connecting head and tail coz we need to input nodes between them
        self.head.next = self.tail
        self.tail.prev = self.head

    def addToTail(self, node):
        previous_node = self.tail.prev
        previous_node.next = node
        node.prev = previous_node
        node.next = self.tail
        self.tail.prev = node
        # previous_node = self.tail.prev
        # previous_node.next = node
        # self.tail.prev = node
        # node.next = self.tail
        # node.prev = previous_node

    def removeNode(self, node):
        previous_node = node.prev
        next_node = node.next
        previous_node.next = next_node
        next_node.prev = previous_node

    def get(self, key: int):
        # if key is present in cache
        if key in self.cache:
            # update most recently used
            self.removeNode(self.cache[key])
            self.addToTail(self.cache[key])
            # just return value
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int):
        # if key is present in cache
        if key in self.cache:
            # node already exists so remove
            self.removeNode(self.cache[key])
        elif self.capacity <= len(self.cache):
            # remove LRU node from hashmap and linked list
            # which is left most just next to head
            lru = self.head.next
            # remove the LRU from LL
            self.removeNode(lru)
            # remove the LRU from hashmap
            del self.cache[lru.key]
        # make new node and add node to hash map
        self.cache[key] = Listnode(key, value)
        # adding to tail coz MRU
        self.addToTail(self.cache[key])
