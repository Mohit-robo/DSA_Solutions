'''
Write a program to reverse an array or string

https://www.geeksforgeeks.org/write-a-program-to-reverse-an-array-or-string/
'''

## Iterative method

'''
1) Initialize start and end indexes as start = 0, end = n-1 
2) In a loop, swap arr[start] with arr[end] and change start and end as follows : 
start = start +1, end = end - 1
'''

def reverse_list_itr(arr):
    
    start = 0
    end = len(arr) - 1

    while start < end:
        arr[start],arr[end] = arr[end],arr[start] 

        start += 1
        end -= 1

A = [1, 2, 3, 4, 5, 6]
print(A)
reverse_list_itr(A)
print("Reversed list is")
print(A)



## Recursive method
'''
1) Initialize start and end indexes as start = 0, end = n-1 
2) Swap arr[start] with arr[end] 
3) Recursively call reverse for rest of the array.
'''


def reverse_list_rec(arr,start,end ):
    
    if start >= end:
        return 
    arr[start],arr[end] = arr[end],arr[start] 
    reverse_list_rec(arr,start + 1,end - 1)

A = [1, 2, 3, 4, 5, 6]
print(A)
reverse_list_rec(A,0,5)
print("Reversed list is")
print(A)