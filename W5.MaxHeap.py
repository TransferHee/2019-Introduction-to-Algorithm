class MaxHeap:
    
    def __init__(self):
        self.queue = [None]
    
    def insert(self, value):
        ## Insert a new value into heap 
        """
        Input:  value
        Output: None
        """
        self.queue.append(value)

        i=len(self.queue)-1

        while i>1:
            parent=i//2
            if self.queue[parent]<self.queue[i]:
                self.queue[parent],self.queue[i]=self.queue[i],self.queue[parent]
                i=parent
            else:
                break
            
        
    def delete(self):
        ## Delete root node
        """
        Input:  None
        Output: if heap is empty print('Heap is empty')
                return deleted value
        """
        if len(self.queue) == 1:
            print("Heap is empty")
            return
        
        item = self.queue[1]
        self.queue[1] = self.queue[len(self.queue)-1]
        self.queue[len(self.queue)-1]= item
        
        self.queue.pop()
        
        i = 1
        while i <= len(self.queue)-1:
            # -------------Fill in the blank
            # HINT- left = i*2
            #     - right = i*2 + 1
            
            left=i*2
            right=i*2+1
            largest=i
            if i*2<=len(self.queue)-1 and self.queue[i]<self.queue[i*2]:
                largest=left
            if i*2+1<len(self.queue) and self.queue[i]>self.queue[i*2+1]:
                largest=right

            if largest !=i:
                self.queue[i],self.queue[largest]=self.queue[largest],self.queue[i]
                i=largest
            else:
                break
    

        return item

def main():

    maxheap = MaxHeap()
    
    maxheap.insert(5)
    maxheap.insert(7)
    maxheap.insert(6)
    maxheap.insert(9)
    maxheap.insert(2)
    print(maxheap.queue)
    maxheap.insert(4)
    maxheap.insert(3)
    maxheap.insert(2)
    maxheap.insert(8)
    print(maxheap.queue)
    
    maxheap.delete()
    print(maxheap.queue)
    print(maxheap.delete())
    
main()
