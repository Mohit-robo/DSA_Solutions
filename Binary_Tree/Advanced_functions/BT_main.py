## Class to add users
from tkinter.tix import Tree


class User:
    def __init__(self, username, name, email):
        self.username = username
        self.name = name
        self.email = email
        
    def __repr__(self):
        return "User(username='{}', name='{}', email='{}')".format(self.username, self.name, self.email)
    
    def __str__(self):
        return self.__repr__()

## Class to add user data
class UserDatabase:
    def __init__(self):
        self.users = []
    
    def insert(self, user):
        i = 0
        while i < len(self.users):
            # Find the first username greater than the new user's username
            if self.users[i].username > user.username:
                break
            i += 1
        self.users.insert(i, user)
    
    def find(self, username):
        for user in self.users:
            if user.username == username:
                return user
    
    def update(self, user):
        target = self.find(user.username)
        target.name, target.email = user.name, user.email
        
    def list_all(self):
        return self.users

def parse_tuple(data):
    print(data)
    if isinstance(data, tuple) and len(data) == 3:
        node = TreeNode(data[1])
        node.left = parse_tuple(data[0])
        node.right = parse_tuple(data[2])
    elif data is None:
        node = None
    else:
        node = TreeNode(data)
    return node

## Class to create a basic binary tree
class TreeNode:
    def __init__(self, key, value=None):
        
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

    '''
    The height/depth of a binary tree is defined as the length of the longest path from its root node to a leaf.
    It can be computed recursively
    '''
    def height(self):
        if self is None:
            return 0
        return 1 + max(TreeNode.height(self.left), TreeNode.height(self.right))
    
    def size(self):
        if self is None:
            return 0
        return 1 + TreeNode.size(self.left) + TreeNode.size(self.right)

    '''
    A traversal refers to the process of visiting each node of a tree exactly once.
    Visiting a node generally refers to adding the node's key to a list. 
    There are three ways to traverse a binary tree and return the list of visited keys:
    
    1. Inorder traversal

    Traverse the left subtree recursively inorder.
    Traverse the current node.
    Traverse the right subtree recursively inorder.

    2. Preorder traversal

    Traverse the current node.
    Traverse the left subtree recursively preorder.
    Traverse the right subtree recursively preorder.

    3. Postorder traversal

    Traverse the left subtree recursively preorder.
    Traverse the right subtree recursively preorder.
    Traverse the current node.

    '''
    def traverse_in_order(self):
        if self is None: 
            return []
        return (TreeNode.traverse_in_order(self.left) + 
                [self.key] + 
                TreeNode.traverse_in_order(self.right))
    
    def traverse_pre_order(self):
        if self is None: 
            return []
        return([self.key] +
            TreeNode.traverse_pre_order(self.left) +
            TreeNode.traverse_pre_order(self.right))

    def traverse_post_order(self):
        if self is None: 
            return []
        return(TreeNode.traverse_post_order(self.left) +
            TreeNode.traverse_post_order(self.right)+
            [self.info])

    '''
    Helper function to display all the keys in a tree-like structure for easier visualization.
    '''
    def display_keys(self, space='\t', level=0):
        # If the node is empty
        if self is None:
            print(space*level + '∅')
            return   

        # If the node is a leaf 
        if self.left is None and self.right is None:
            print(space*level + str(self.key))
            return

        # If the node has children
        TreeNode.display_keys(self.right, space, level+1)
        print(space*level + str(self.key))
        TreeNode.display_keys(self.left,space, level+1)    
    
    def to_tuple(self):
        if self is None:
            return None
        if self.left is None and self.right is None:
            return self.key
        return TreeNode.to_tuple(self.left),  self.key, TreeNode.to_tuple(self.right)
    
    def __str__(self):
        return "BinaryTree <{}>".format(self.to_tuple())
    
    def __repr__(self):
        return "BinaryTree <{}>".format(self.to_tuple())
    
    @staticmethod    
    def parse_tuple(data):
        if data is None:
            node = None
        elif isinstance(data, tuple) and len(data) == 3:
            node = TreeNode(data[1])
            node.left = TreeNode.parse_tuple(data[0])
            node.right = TreeNode.parse_tuple(data[2])
        else:
            node = TreeNode(data)
        return node


    '''
    A binary search tree or BST is a binary tree that satisfies the following conditions:

        The left subtree of any node only contains nodes with keys less than the node's key
        The right subtree of any node only contains nodes with keys greater than the node's key

    '''
    def remove_none(nums):
        return [x for x in nums if x is not None]

    def is_bst(self):
        if self is None:
            return True, None, None
        
        is_bst_l, min_l, max_l = TreeNode.is_bst(self.left)
        is_bst_r, min_r, max_r = TreeNode.is_bst(self.right)
        
        is_bst_node = (is_bst_l and is_bst_r and 
                (max_l is None or self.key > max_l) and 
                (min_r is None or self.key < min_r))
        
        min_key = min(TreeNode.remove_none([min_l, self.key, min_r]))
        max_key = max(TreeNode.remove_none([max_l, self.key, max_r]))
        
        # print(node.key, min_key, max_key, is_bst_node)
            
        return is_bst_node, min_key, max_key

    ## Insertion into BST
    '''
    Starting from the root node, we compare the key to be inserted with the current node's key
    If the key is smaller, we recursively insert it in the left subtree (if it exists) or attach it as as the left child if no left subtree exists.
    If the key is larger, we recursively insert it in the right subtree (if it exists) or attach it as as the right child if no right subtree exists.

    '''
    def insert(self,key,value):
        if self is None:
            self = TreeNode(key, value)
        elif key < self.key:
            self.left = TreeNode.insert(self.left, key, value)
            self.left.parent = self
        elif key > self.key:
            self.right = TreeNode.insert(self.right, key, value)
            self.right.parent = self
        return self
    
    # Finding a Node in BST

    def find(self, key):
        if self is None:
            return None
        if key == self.key:
            return self
        if key < self.key:
            return TreeNode.find(self.left, key)
        if key > self.key:
            return TreeNode.find(self.right, key)

    # Updating a value in a BST
    # We can use find to locate the node to be updated, and simply update it's value.

    def update(self, key, value):
        target = TreeNode.find(self, key)
        if target is not None:
            target.value = value

    ## The nodes can be listed in sorted order by performing an inorder traversal of the BST.

    def list_all(self):
        if self is None:
            return []
        return TreeNode.list_all(self.left) + [(self.key, self.value)] + TreeNode.list_all(self.right)


    #Balanced Binary Trees
    '''
    Here's a recursive strategy:

        Ensure that the left subtree is balanced.
        Ensure that the right subtree is balanced.
        Ensure that the difference between heights of left subtree and right subtree is not more than 1.
    '''
    def is_balanced(self):
        if self is None:
            return True, 0
        balanced_l, height_l = TreeNode.is_balanced(self.left)
        balanced_r, height_r = TreeNode.is_balanced(self.right)
        balanced = balanced_l and balanced_r and abs(height_l - height_r) <=1
        height = 1 + max(height_l,height_r)
        return balanced, height

    '''
        We create a balanced BST from a sorted list/array of key-value pairs.
        We can use a recursive strategy here, turning the middle element of the list into the root, 
        and recursively creating left and right subtrees.
    
    '''

    def make_balanced_bst(data, lo=0, hi=None, parent=None):
        if hi is None:
            hi = len(data) - 1
        if lo > hi:
            return None
        
        mid = (lo + hi) // 2
        key, value = data[mid]

        root = TreeNode(key, value)
        root.parent = parent
        root.left = TreeNode.make_balanced_bst(data, lo, mid-1, root)
        root.right = TreeNode.make_balanced_bst(data, mid+1, hi, root)
        
        return root

    def balance_bst(self):
        return TreeNode.make_balanced_bst(TreeNode.list_all(self))
