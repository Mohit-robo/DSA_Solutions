'''

    QUESTION : As a senior backend engineer,
               you are tasked with developing a fast in-memory data structure to manage profile information (username, name and email) 
               for 100 million users. It should allow the following operations to be performed efficiently:

        Insert the profile information for a new user.
        Find the profile information of a user, given their username
        Update the profile information of a user, given their usrname
        List all the users of the platform, sorted by username

    You can assume that usernames are unique.

'''

from BT_main import TreeNode,User

aakash = User('aakash', 'Aakash Rai', 'aakash@example.com')
biraj = User('biraj', 'Biraj Das', 'biraj@example.com')
hemanth = User('hemanth', 'Hemanth Jain', 'hemanth@example.com')
jadhesh = User('jadhesh', 'Jadhesh Verma', 'jadhesh@example.com')
siddhant = User('siddhant', 'Siddhant Sinha', 'siddhant@example.com')
sonaksh = User('sonaksh', 'Sonaksh Kumar', 'sonaksh@example.com')
vishal = User('vishal', 'Vishal Goel', 'vishal@example.com')
mohit = User('mohit', 'Mohit Goel', 'mohit@example.com')

users = [aakash, biraj, hemanth, jadhesh, siddhant, sonaksh, vishal]

class TreeMap():
    
    def __init__(self):
        self.root  = None

    ## To update
    def __setitem__(self,key,value):
        node = TreeNode.find(self.root,key)
        if not node:
            self.root = TreeNode.insert(self.root,key,value)
        else:
            TreeNode.update(self.root,key,value)

    ## To find item
    def __getitem__(self,key):
        node = TreeNode.find(self.root,key)
        return node.value if node else None

    ## List elements
    def __iter__(self):
        return (x for x in TreeNode.list_all(self.root))    ## returns a generator and not a list

    ## Length of the tree
    def __len__(self):
        return TreeNode.size(self.root)

    ## display the tree
    def display(self):
        return TreeNode.display_keys(self.root)

## The advantage of using these special methods insted of user defined methods are explained below on each step:

treemap = TreeMap()
treemap.display()

# 1. Inserting a new Node/user to the tree/Database

'''
The same operation with user defined method would be performed in this way:

treemap.insert(biraj.username, biraj)
treemap.insert(sonaksh.username, sonaksh)
treemap.insert(aakash.username, aakash)

But instead the below mentioned method is user-friendly

'''

treemap['aakash'] = aakash
treemap['jadhesh'] = jadhesh
treemap['sonaksh'] = sonaksh

treemap.display()

# 2. Finding a user/node and diplaying the data
'''
node_jadhesh = treemap.find('jadhesh')
node_jadhesh.key, node_hemantjadhesh.value
'''

print(treemap['jadhesh'])

# 3. Printing the len of the tree

'''
treemap.height()

using len(treemap) is user friendly as we keep on using it in day-to-day codes 
'''
print(len(treemap))

'''
For printing multiple users

as the __iter__ method returns as generator, it makes possible to print all user keys and values by looping through each node
'''
for key, value in treemap:
    print(key, value)

# 4. Updating a node/user information

'''
treemap.update('aakash', User('aakash', 'Aakash N S', 'aakashns@example.com'))

The below mentioned way is more user frinedly to write and understand
'''
treemap['aakash'] = User(username='aakash', name='Aakash N S', email='aakashns@example.com')