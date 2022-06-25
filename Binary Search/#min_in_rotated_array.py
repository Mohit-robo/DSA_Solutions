'''
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

    [4,5,6,7,0,1,2] if it was rotated 4 times.
    [0,1,2,4,5,6,7] if it was rotated 7 times.

Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.

 
Example 1:

Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.

Example 2:

Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.

Explanation: https://www.youtube.com/watch?v=nIVW4P8b1VA
'''

class Solution:
    def findMin(nums: list) -> int:
     
    ## Soluiton 1: O (log N) -- time complexity  53 ms
        res = nums[0]
        l,r = 0,len(nums)-1

        while l<r:
            if nums[l]<nums[r]:
                res = min(res,nums[l])
                break

            m = (l + r)//2
            res = min(nums[m],res)

            if nums[m] >= nums[l]:
                l = m+1
            else:
                r = m-1
        return res
              
        
    # Solution 2: O(n) -- time complexity   43 ms
        '''
        
        for i in range(len(nums)):
            if nums[i] < nums[i-1]:
                return nums[i]
        
        '''
            
nums = [11,13,15,17]
# nums =  [3,4,5,1,2]
# nums = [4,5,6,7,0,1,2]
print(Solution.findMin(nums))