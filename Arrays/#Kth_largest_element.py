'''
Kth Largest Element in an Array

Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4

'''

import random

class Solution:
    def findKthLargest(nums: list, k: int) -> int:

        pivot = random.choice(nums)
    
        left = [x for x in nums if x > pivot]
        mid = [x for x in nums if x == pivot]
        right = [x for x in nums if x < pivot]
        
        # print(left,mid,right,nums)
        L,M = len(left),len(mid)
        if k <= L:
            return Solution.findKthLargest(left,k)
        elif k > (L+M):
            return Solution.findKthLargest(right,k-(L+M))
        else:
            return mid[0]

    ## Solution 2

        # nums.sort()
        # if k ==1:
        #     return nums[-1]
        
        # return nums[len(nums)-k]

nums = [3,2,3,1,2,4,5,5,6]
k = 4
print(Solution.findKthLargest(nums,k))