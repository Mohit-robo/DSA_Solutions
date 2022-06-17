'''
You are given a read only array of n integers from 1 to n.

Each integer appears exactly once except A which appears twice and B which is missing.

Return A and B.

Note: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Note that in your output A should precede B.

Example:

Input:[3 1 2 5 3] 

Output:[3, 4] 

A = 3, B = 4

'''

class Solution:
    # @param A : tuple of integers
    # @return a list of integers

    ## Solution 1:  Traverse the array. While traversing, use the absolute value of every element as an index and 
                    # make the value at this index as negative to mark it visited.
                    # If something is already marked negative then this is the repeating element.
                    # To find missing, traverse the array again and look for a positive value.
    
    
    def printTwoElements( arr, size):
        for i in range(size):
            if arr[abs(arr[i])-1] > 0:
                arr[abs(arr[i])-1] = -arr[abs(arr[i])-1]
            else:
                print("The repeating element is ", abs(arr[i]))
                
        for i in range(size):
            if arr[i]>0:
                print("and the missing element is ", i + 1)
    
    ## Solution 2: repeated number = x = Sum of all elements of A minus sum of unique elements of A  --> set(A) only has unique elements and no duplicates
                # k =  Sum of all elements of A minus sum of first n numbers
                # miss number = x-k               


    def repeatedNumber(self, A):
        n = len(A)
        x = sum(A) - sum(set(A))
        k = sum(A) - int(n*(n+1)/2)
    
        return [x,x-k]

arr = [7, 3, 4, 5, 5, 6, 2]
print(Solution.printTwoElements(arr))