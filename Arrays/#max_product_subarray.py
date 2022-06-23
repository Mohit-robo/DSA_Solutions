'''
Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

A subarray is a contiguous subsequence of the array.

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

https://leetcode.com/problems/maximum-product-subarray/

Explanation: https://www.youtube.com/watch?v=lXVy6YWFcRM

'''

class Solution:
    def maxSubArray(nums: list) -> int:
        
        res = max(nums)
        curMax,curMin = 1,1

        for n in nums:
            # If element is 0, reset to min and max to 1
            if n == 0:
                curMin,curMax = 1,1
                continue
            
            tmp = curMax * n
            print(curMin,curMax)    
            curMax = max(tmp,n*curMin,n)
            curMin = min(tmp,n*curMin,n)    
            res = max(res,curMax)

        return res
nums =[-2,0,-1]

print(Solution.maxSubArray(nums))