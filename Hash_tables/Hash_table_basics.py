'''
Objective: 

Implement a HashTable class which supports the following operations:

    Insert: Insert a new key-value pair
    Find: Find the value associated with a key
    Update: Update the value associated with a key
    List: List all the keys stored in the hash table

--> Dictionaries in Python are implemented using a data structure called hash table. A hash table uses a list/array to store the key-value pairs,
    and uses a hashing function to determine the index for storing or retrieving the data associated with a given key. 
'''

'''

Hashing Function

A hashing function is used to convert strings and other non-numeric data types into numbers, which can then be used as list indices. For instance, if a hashing function converts the string "Aakash" into the number 4, then the key-value pair ('Aakash', '7878787878') will be stored at the position 4 within the data list.

Here's a simple algorithm for hashing, which can convert strings into numeric list indices.

    Iterate over the string, character by character
    Convert each character to a number using Python's built-in ord function.
    Add the numbers for each character to obtain the hash for the entire string
    Take the remainder of the result with the size of the data list
'''

def get_index(data_list, a_string):
    # Variable to store the result (updated after each iteration)
    result = 0
    
    for a_character in a_string:
        # Convert the character to a number (using ord)
        a_number = ord(a_character)
        # Update result by adding the number
        result += a_number
    
    # Take the remainder of the result with the size of the data list
    list_index = result % len(data_list)
    return list_index

MAX_HASH_TABLE_SIZE = 4096        ### Can be changed
data_list = [None] * MAX_HASH_TABLE_SIZE

ord('M') + ord('o') + ord('h') + ord('i') + ord('t') 
get_index(data_list, 'Mohit') == 513   ## Returns True
get_index(data_list, 'mohit') == 513   ## Returns False

'''
Collisions: 

The addition of the ord values of M o h i t == h i t M o, another example silent and listen have same value when added up.
This causes the key assigned to the value to be overwritten. 

To handle collisions we'll use a technique called linear probing. Here's how it works:

    While inserting a new key-value pair if the target index for a key is occupied by another key, then we try the next index, followed by the next and so on till we the closest empty location.

    While finding a key-value pair, we apply the same strategy, but instead of searching for an empty location, we look for a location which contains a key-value pair with the matching key.

    While updating a key-value pair, we apply the same strategy, but instead of searching for an empty location, we look for a location which contains a key-value pair with the matching key, and update its value.

'''

def get_valid_index(data_list, key):
    # Start with the index returned by get_index
    idx = get_index(data_list, key)
    
    while True:
        # Get the key-value pair stored at idx
        kv = data_list[idx]
        
        # If it is None, return the index
        if kv is None:
            return idx
        
        # If the stored key matches the given key, return the index
        k, v = kv
        if k == key:
            return idx
        
        # Move to the next index
        idx += 1
        
        # Go back to the start if you have reached the end of the array
        if idx == len(data_list):
            idx = 0

# Create an empty hash table
data_list2 = [None] * MAX_HASH_TABLE_SIZE

# New key 'listen' should return expected index
get_valid_index(data_list2, 'listen') == 655  ## Shall return True

# Insert a key-value pair for the key 'listen'
data_list2[get_index(data_list2, 'listen')] = ('listen', 99)

# Colliding key 'silent' should return next index
get_valid_index(data_list2, 'silent') == 656    # Shall return True

'''
You can see that, as the keys collide the later value is assigned the next empty key.
'''

# Hash Table with Linear Probing

class ProbingHashTable:
    def __init__(self, max_size=MAX_HASH_TABLE_SIZE):
        # 1. Create a list of size `max_size` with all values None
        self.data_list = [None] * max_size
      
    def insert(self, key, value):
        # 1. Find the index for the key using get_valid_index
        idx = get_valid_index(self.data_list, key)
        
        # 2. Store the key-value pair at the right index
        self.data_list[idx] = key,value
    
    def find(self, key):
        # 1. Find the index for the key using get_valid_index
        idx = get_valid_index(self.data_list, key)
        
        # 2. Retrieve the data stored at the index
        kv = self.data_list[idx]
        
        # 3. Return the value if found, else return None
        return None if kv is None else kv[1]
    
    def update(self, key, value):

        # 1. Find the index for the key using get_valid_index
        idx = get_valid_index(self.data_list, key)
        
        # 2. Store the new key-value pair at the right index
        self.data_list[idx] = key,value

    def list_all(self):
        # 1. Extract the key from each key-value pair 
        return [kv[0] for kv in self.data_list if kv is not None]


# Create a new hash table
probing_table = ProbingHashTable()

# Insert a value
probing_table.insert('listen', 99)

# Check the value
print(probing_table.find('listen') == 99)


# Insert a colliding key
probing_table.insert('silent', 200)

# Check the new and old keys
print(probing_table.find('listen') == 99 and probing_table.find('silent') == 200)

# Update a key
probing_table.insert('listen', 101)

# Check the value
probing_table.find('listen') == 101

print(probing_table.list_all())