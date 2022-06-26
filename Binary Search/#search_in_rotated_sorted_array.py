'''
https://leetcode.com/problems/search-in-rotated-sorted-array/

There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

https://www.youtube.com/watch?v=U8XENwh8Oy8
'''

class Solution:
    # Solution 1
    def search( nums: list, target: int) -> int:
        l,r = 0,len(nums)-1
        
        while l <= r:
            m = (l + r)//2
            # print(m)
            
            if target == nums[m]:
                return m

            if nums[l] <= nums[m] : 
                
                if target > nums[m] or target < nums[l]:
                    l = m+1
                else:
                    r = m - 1

            else:
                if target < nums[m] or target > nums[r]:
                    
                    r = m-1
                else:
                    l = m + 1 

        return -1
    
    # Solution 2
    def search(self, nums: list, target: int) -> int:
        if target not in nums:
            return -1

        for i in range(len(nums)):
            if nums[i] == target:
                return i

nums = [4,5,6,7,0,1,2]
target = 0
print(Solution.search(nums,target))