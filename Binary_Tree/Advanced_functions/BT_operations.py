from tkinter.tix import Tree
from BT_main import User,UserDatabase,TreeNode,parse_tuple

'''   MAKE SURE TO ADD PRINT FUNCTION TO THE OPERTAIONS      '''

## Some example inputs & outputs.
'''
aakash = User('aakash', 'Aakash Rai', 'aakash@example.com')
biraj = User('biraj', 'Biraj Das', 'biraj@example.com')
hemanth = User('hemanth', 'Hemanth Jain', 'hemanth@example.com')
jadhesh = User('jadhesh', 'Jadhesh Verma', 'jadhesh@example.com')
siddhant = User('siddhant', 'Siddhant Sinha', 'siddhant@example.com')
sonaksh = User('sonaksh', 'Sonaksh Kumar', 'sonaksh@example.com')
vishal = User('vishal', 'Vishal Goel', 'vishal@example.com')
mohit = User('mohit', 'Mohit Goel', 'mohit@example.com')

users = [aakash, biraj, hemanth, jadhesh, siddhant, sonaksh, vishal]
'''

## Uncomment to add,find and update user data
'''
database = UserDatabase()

database.insert(hemanth)
database.insert(aakash)
database.insert(siddhant)

user = database.find('siddhant')

database.update(User(username='siddhant', name='Siddhant U', email='siddhantu@example.com'))

database.list_all()
'''

### Creating a basic binary tree

'''
# 1. Creating Manually 

node0 = TreeNode(3)
node1 = TreeNode(4)
node2 = TreeNode(5)

node0.left = node1
node0.right = node2

tree = node0

tree.key,tree.left.key,tree.right.key
'''

# 2.Automated

'''
tree_tuple[1] --> Root Node i.e --> 2 --> applicable to sub-tuples as well 
--> eg: (None,3,4) --> 3 is the node, None to left and 4 to right

elemnts to left --> added to the left of the node
elemnts to right --> added to the right of the node 

tree_tuple = ((1,3,None), 2, ((None, 3, 4), 5, (6, 7, 8)))   

tree2 = parse_tuple(((1,3,None), 2, ((None, 3, 4), 5, (6, 7, 8))))
tree2.right.left.right.key, tree2.right.right.left.key, tree2.right.right.right.key

## Performing various operation from class TreeNode.

tree = TreeNode.parse_tuple(tree_tuple)
tree.display_keys('  ')
tree.height()
tree.size()
tree.traverse_in_order()

tree.is_bst()  ## Checking if the tree is a Binary Search Tree
'''

'''
## Storing Key-Value Pairs using BSTs

# Level 0
tree3 = TreeNode(jadhesh.username, jadhesh)

# Level 1
tree3.left = TreeNode(biraj.username, biraj)
tree3.right = TreeNode(sonaksh.username, sonaksh)

# View Level 1
tree3.left.key, tree3.left.value, tree3.right.key, tree3.right.value

tree3.display_keys()

## Insertion Operation

tree3.insert(biraj.username, biraj)
tree3.insert(sonaksh.username, sonaksh)
tree3.insert(aakash.username, aakash)
tree3.insert(hemanth.username, hemanth)
tree3.insert(siddhant.username, siddhant)
tree3.insert(vishal.username, vishal)
tree3.insert(mohit.username, mohit)

tree3.display_keys()

## Finding the Node
node = tree3.find('hemanth')
node.key, node.value

## Updating the Node

tree3.update('hemanth', User('hemanth', 'Hemanth J', 'hemanthj@example.com'))
node_hemant = tree3.find('hemanth')
node_hemant.key, node_hemant.value

tree3.is_balanced()

## Balancing unbalanced trees. 

data = [(user.username, user) for user in users]
data

tree1 = None

for user in users:
    tree1 = TreeNode.insert(tree1, user.username, user)  ## Here we enter nodes alphabeltical wise, this ,akes it an unbalanced tree

tree1.display_keys()

tree2 = tree1.balance_bst()
tree2.display_keys()

'''
