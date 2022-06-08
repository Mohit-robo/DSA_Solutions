'''
Complete the function preOrder in the editor below, which has

parameter: a pointer to the root of a binary tree. It must print the values in the tree's preorder traversal as a single line of space-separated values.

Input Format

Our test code passes the root node of a binary tree to the preOrder function.

Output Format

Print the tree's preorder traversal as a single line of space-separated values.

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

1 2 5 3 4 6 

Explanation

The preorder traversal of the binary tree is printed. 

Link: https://www.hackerrank.com/challenges/tree-preorder-traversal

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

def preOrder(root):
    p = root
    if p is None:
        return
    preOrder(p.left)
    preOrder(p.right)
    print(p.info, end=' ')

def traverse_pre_order(node):
    if node is None: 
        return []
    return([node.info] +
           traverse_pre_order(node.left) +
           traverse_pre_order(node.right))


def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

   stack = [root]
   res = []
   while stack:
       node = stack.pop()
       if node:
           stack.append(node.right)
           stack.append(node.left)
           stack.append(node)
       else:
           if stack:
               node = stack.pop()
               res.append(node.val)
    
        return res
    
solution = Solution()
lst = (solution.inorderTraversal(TreeNode()))

tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

print(traverse_pre_order(tree.root))
