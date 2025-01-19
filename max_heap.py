import heapq

class MaxHeap:
    def __init__(self, data=[]):
        data = [-x for x in data]
        heapq.heapify(data)
        self.data = data
    
    def push(self, ele):
        heapq.heappush(self.data, -ele)
    
    def pop(self):
        return -heapq.heappop(self.data)
    
    def peek(self):        
        return -self.data[0]
    
    def __repr__(self):
        return str(self.data)
    
    def __len__(self):
        return len(self.data)