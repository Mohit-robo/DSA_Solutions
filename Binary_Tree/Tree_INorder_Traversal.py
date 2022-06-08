'''
In this challenge, you are required to implement inorder traversal of a tree.

Complete the inOrder function in your editor below, which has

parameter: a pointer to the root of a binary tree. It must print the values in the tree's inorder traversal as a single line of space-separated values.

Input Format

Our hidden tester code passes the root node of a binary tree to your $inOrder* function.

Output Format

Print the tree's inorder traversal as a single line of space-separated values.

Sample Input

     1
      \
       2
        \
         5
        /  \
       3    6
        \
         4  

Sample Output

1 2 3 4 5 6 

Explanation

The tree's inorder traversal results in 1 2 3 4 5 6 as the required result. 

Link: https://www.hackerrank.com/challenges/tree-inorder-traversal

'''

class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""

## Recursive Method
def inOrder(root):
    #Write your code here
    p = root
    if p is None:
        return
    inOrder(p.left)
    print(p.info, end=' ')
    inOrder(p.right)
    
def in_order_traverse(root):
    
    if root is None:
        return []
    
    return (in_order_traverse(root.left)+
            [root.info] +
            in_order_traverse(root.right))

## Iterative Method

def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

   stack = [root]
   res = []
   while stack:
       node = stack.pop()
       if node:
           stack.append(node.right)
           stack.append(node)
           stack.append(node.left)
       else:
           if stack:
               node = stack.pop()
               res.append(node.val)

   return res
    

tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

print(in_order_traverse(tree.root))
print(inorderTraversal(arr)
