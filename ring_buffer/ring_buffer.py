class RingBuffer:
    def __init__(self, capacity):
        self.store=[]
        self.capacity=capacity
        self.location=0

    def append(self, item):
        if(len(self.store)==self.capacity):
            self.store[self.location]=item
            if(self.location<self.capacity-1):
                self.location+=1
            else:
                self.location = 0
        else:
            self.store.append(item)


    def get(self):
        return self.store