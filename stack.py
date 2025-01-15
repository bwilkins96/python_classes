class Stack:
    def __init__(self, data=[]):
        self.data = []
    
    def pop(self):
        return self.data.pop()
    
    def peek(self):
        return self.data[-1]
    
    def push(self, ele):
        self.data.append(ele)
    
    def empty(self):
        return len(self.data) == 0
    
    def __repr__(self):
        return f'bottom - {self.data} - top'
    
    def __len__(self):
        return len(self.data)