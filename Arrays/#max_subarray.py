'''
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

https://leetcode.com/problems/maximum-subarray/

'''

class Solution:
    def maxSubArray(nums: list) -> int:
        
        dp = []
        dp.append(nums[0])
        dp_largest_sum = dp[0]
        
        for i in range (1,len(nums)):
                        
            dp.append(max(dp[i-1] + nums[i],nums[i]))
            if dp[i] > dp_largest_sum:
                dp_largest_sum = dp[i]
        return dp_largest_sum


nums = [5,4,-1,7,8]
print(Solution.maxSubArray(nums))