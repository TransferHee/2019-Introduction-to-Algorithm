
class Node:
    def __init__(self,item):
        self.item=item
        self.prev=None
        self.next=None

class Dlist:
    def __init__(self):
        self.head=None

    def is_empty(self):
        return self.head==None

    def add(self,item):
        newnode=Node(item)
        if self.is_empty():
            self.head=newnode
        else:
            newnode.next=self.head
            self.head.prev=newnode
            self.head=newnode

    def append(self,item):
        newnode=Node(item)
        if self.is_empty():
            self.head=newnode
        else:
            current=self.head
            while current.next:
                current=current.next
            current.next=newnode
            newnode.prev=current

    def insert_after(self,item,x):
        current=self.head
        newnode=Node(item)
        while(1):
            if current.item==x:
                break
            if current.next==None:
                print("There is no node")
                return False
            current=current.next
        nnode=current.next
        current.next=newnode
        newnode.prev=current
        newnode.next=nnode
        nnode.prev=newnode


    def insert_before(self,item,x):
        if self.head==None:
            print("List is empty")
        else:
            current=self.head
            found=False
            while current !=None and not found:
                if current.item==x:
                    found=True
                else:
                    current=current.next
            if found==False:
                print("No item")
            else:
                t=Node(item)
                t.next=current.next
                t.prev=current
                if current.next !=None:
                    a=current.next
                    a.prev=t
                current.next=t

    def pop_first(self):
        if self.is_empty():
            print("List is empty!!")
        else:
            current=self.head
            if current.next==None:
                self.head=None
            else:
                self.head=current.next
                self.head.prev=None


    def pop_last(self):
        if self.is_empty():
            print("List is empty!!")
        else:
            current=self.head
            if current.next==None:
                self.head=None
            else:
                while current.next:
                    current=current.next
                pnode=current.prev
                pnode.next=None

    def delete(self,item):
        if self.is_empty():
            print("List is empty!!")
        else:
            current=self.head
            while(1):
                if current.item==item:
                    break
                if current.next==None:
                    print("There is no node")
                    return False
                current=current.next
            if current.next==None and current==self.head:
                self.head=None
            elif current.next==None:
                pnode=current.prev
                pnode.next=None
            elif current==self.head:
                nnode=current.next
                self.head=nnode
                nnode.prev=None
            else:
                pnode=current.prev
                nnode=current.next
                pnode.next=nnode
                nnode.prev=pnode
                
            
        
