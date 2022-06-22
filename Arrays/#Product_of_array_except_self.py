'''
https://leetcode.com/problems/product-of-array-except-self/

Algorithm: 

    Create two array prefix and suffix of length n, i.e length of the original array, initialize prefix[0] = 1 and suffix[n-1] = 1 and also another array to store the product.
    Traverse the array from second index to end.
    For every index i update prefix[i] as prefix[i] = prefix[i-1] * array[i-1], i.e store the product upto i-1 index from the start of array.
    Traverse the array from second last index to start.
    For every index i update suffix[i] as suffix[i] = suffix[i+1] * array[i+1], i.e store the product upto i+1 index from the end of array
    Traverse the array from start to end.
    For every index i the output will be prefix[i] * suffix[i], the product of the array element except that element.

'''
class Solution:
    def productExceptSelf(nums: list) -> list:
        
        n = len(nums)
        # Base case
        if n == 1:
            print(0)
            return
    
        i, temp = 1, 1
    
        # Allocate memory for the product array
        prod = [1 for i in range(n)]
    
        # Initialize the product array as 1
    
        # In this loop, temp variable contains product of
        # elements on left side excluding arr[i]
        for i in range(n):
            prod[i] = temp
            temp *= nums[i]
    
        # Initialize temp to 1 for product on right side
        temp = 1
    
        # In this loop, temp variable contains product of
        # elements on right side excluding nums[i]
        for i in range(n - 1, -1, -1):
            prod[i] *= temp
            temp *= nums[i]

        return prod

# nums = [1,2,3,4]
nums = [-1,1,0,-3,3]
print(Solution.productExceptSelf(nums))