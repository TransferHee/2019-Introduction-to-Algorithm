class Node:

    def __init__(self,value):
        self.value=value
        self.next=None


class LinkedList:

    def __init__(self):
        self.head=None

    def add_last(self,item):
        newnode=Node(item)
        if self.is_empty():
            self.head=newnode
        else:
            current=self.head
            while current.next:
                current=current.next
            current.next=newnode

    def add_first(self,item):
        if self.is_empty():
            self.head=Node(item)
        else:
            newnode=Node(item)
            newnode.next=self.head
            self.head=newnode

    def add(self,pos,item):
        if pos<=0 or pos>self.get_length()+1:
            print("pos out of length")
        else:
            if pos==1:
                Node(item).next=self.head
                self.head=Node(item)
            else:
                current=self.head
                newnode=Node(item)
                for i in range(pos-2):
                    current=current.next
                newnode.next=current.next
                current.next=newnode

    def delete_last(self):
        if self.is_empty():
            print("list is empty")
        elif self.head.next==None:
            self.head=None
        else:
            current=self.head
            prevnode=None
            while current.next !=None:
                prevnode=current
                current=current.next
            prevnode.next=None

    def delete_first(self):
        if self.is_empty():
            print("xxx")
        else:
            current=self.head
            self.head=current.next


    def display(self):
        if self.is_empty():
            print("There is no node")
        else:
            current=self.head
            while current:
                if current.next !=None:
                    print(current.value,'->',end=' ')
                else:
                    print(current.value)
                current=current.next

    def get_length(self):
        count=0
        if self.is_empty():
            return count
        current=self.head
        while(1):
            if current.next==None:
                return count+1
            else:
                current=current.next
                count+=1

    def is_empty(self):
        return True if not self.head else False

def main():
    
    linked_list = LinkedList()
    
    linked_list.add_last(3)
    linked_list.add_last(7) 
    linked_list.add_last(4) 
    linked_list.display() # Expected Result: linked list values>  3 -> 7 -> 4
    

    linked_list.add_first(1)
    linked_list.add_first(2)
    linked_list.display() # Expected Result: linked list values>  2 -> 1 -> 3 -> 7 -> 4

    linked_list.add(7, 100) # Expected Result: list position out of range !!
    
    linked_list.add(3, 100)
    linked_list.display() # Expected Result: linked list values>  2 -> 1 -> 100 -> 3 -> 7 -> 4
    
    linked_list.delete_first()
    linked_list.delete_last()
    linked_list.display() # Expected Result: linked list values>  1 -> 100 -> 3 -> 7
    
    linked_list.delete_first()
    linked_list.delete_last()
    linked_list.delete_first()
    linked_list.display() # Expected Result: linked list values>  3
    
    linked_list.delete_last()
    linked_list.display() # Expected Result: linked list is empty !!
    
if __name__=="__main__":
    main()



#display 잘보기
#current없을때, current.next없을때, 일반적일때 다생각하기
#current가아니라current.value로 값 출력
    

#if 쓸땐 else도 쓰기
#안그러면 if를 지나고 그 밑도 지날수도있음

#add도 틀림
#pos범위 유의, 마지막에 추가가능하니까 길이+1이상일때 안되는거임


#delete last 틀림
#노드가 없을때, 하나일때, 여러개일때 다생각하기
