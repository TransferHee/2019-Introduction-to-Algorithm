q=[2,4,6,8,10,12,14,16,18,20]


def bs(q,target):
    low=0
    high=len(q)-1


    
    while low<=high:
        mid=(low+high)//2
        if q[mid]==target:
            return True
        elif q[mid]<target:
            low=mid+1
        elif q[mid]>target:
            high=mid-1

    return False

print(bs(q,2))
print(bs(q,3))

def get_node_count(self,node):
    count=0
    if node:
        count=1+get_node_count(node.left)+get_node_count(node.right)

    return count

def get_height(self,node):
    height=0
    if node:
        height=1+max(get_height(node.left),get_height(node.right))

    return height
def preorder(self,node):
    if node:
        print(node.key,end=" ")
        self.preorder(self.left)
        self.preorder(self.right)


print((600*601)/2)
