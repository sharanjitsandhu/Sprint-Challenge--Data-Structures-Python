class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = [None]*capacity

# append method adds elements to the buffer.
    def append(self, item):
        # add to storage based on current (index)
        self.storage[self.current] = item
        if self.current == self.capacity - 1:
            self.current = 0
        else:
            self.current += 1

# get method returns all of the elements in the buffer in a list in their given order.
    def get(self):
        return [item for item in self.storage if item != None]
