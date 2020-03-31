class Node:
    
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    
    def __init__(self):
        self.root = None
    
    def insert(self, current_node, key):
        ## Insert a new node with given key to bst 
        """
        Input:  current_node, key
        Output: None
        """   
        if self.root == None:
            self.root = Node(key)
            
        elif not self.search(self.root, key):
            if current_node.key > key:
                if (current_node.left == None):
                    current_node.left = Node(key)
                else:
                    self.insert(current_node.left, key)
            
            elif current_node.key < key:
                if current_node.right == None:
                    current_node.right = Node(key)
                else:
                    self.insert(current_node.right, key)
    
    def search(self, current_node, key):
        ## Search a given key in bst 
        """
        Input:  current_node, key
        Output: return False if key is not in bst
                return the node if key is in bst
        """
        if self.root == None:
            return False
            
        elif current_node.key == key:
            return current_node
        
        elif current_node.key > key and current_node.left:
            self.search(current_node.left, key)
            
        elif current_node.key < key and current_node.right:
            self.search(current_node.right, key)
    
    def preorder(self, node):
        ## Completed Funtion - DO NOT REMOVE
        ## Display key(s) of the bst in preorder
        if node:  
            print(node.key, end=" ")
            self.preorder(node.left)
            self.preorder(node.right)

    def minValueNode(self, node):
        current = node

        # loop down to find the leftmost leaf
        while (current.left is not None):
            current = current.left

        return current

        # Given a binary search tree and a key, this function

    # delete the key and returns the new root
    def deleteNode(self, root, key):

        # Base Case
        if root is None:
            return root

            # If the key to be deleted is smaller than the root's
        # key then it lies in  left subtree
        if key < root.key:
            root.left = self.deleteNode(root.left, key)

            # If the kye to be delete is greater than the root's key
        # then it lies in right subtree
        elif (key > root.key):
            root.right = self.deleteNode(root.right, key)

            # If key is same as root's key, then this is the node
        # to be deleted
        else:

            # Node with only one child or no child
            if root.left is None:
                temp = root.right
                root = None
                return temp

            elif root.right is None:
                temp = root.left
                root = None
                return temp

            # Node with two children: Get the inorder successor
            # (smallest in the right subtree)
            temp = self.minValueNode(root.right)

            # Copy the inorder successor's content to this node
            root.key = temp.key

            # Delete the inorder successor
            root.right = self.deleteNode(root.right, temp.key)


def main():
    
    bst1 = BinarySearchTree()
    bst1.insert(bst1.root, 60)
    bst1.insert(bst1.root, 25)
    bst1.insert(bst1.root, 100)
    bst1.insert(bst1.root, 35)
    bst1.insert(bst1.root, 17)
    bst1.insert(bst1.root, 80)
    bst1.preorder(bst1.root)

    print()
    
    bst2 = BinarySearchTree()
    bst2.insert(bst2.root, "stupid")
    bst2.insert(bst2.root, "in")
    bst2.insert(bst2.root, "love")
    bst2.insert(bst2.root, "by")
    bst2.insert(bst2.root, "mad")
    bst2.insert(bst2.root, "clown")
    bst2.insert(bst2.root, "and")
    bst2.insert(bst2.root, "soyou")
    bst2.preorder(bst2.root)
    
main()

