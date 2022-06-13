'''
Contains Duplicate:

Given an integer array nums, return true if any value appears at least twice in the array, 
and return false if every element is distinct.
'''

class Solution:
    def containsDuplicate(self, nums: list) -> bool:
        count = 0
        for i in range (len(nums)):
            for j in range (len(nums)):
                if nums[i] == nums[j] and i!=j:
                    count +=1
                      
        if count >=2:
            return True
        else:
            return False

    def containsDuplicate_set(self, nums: list) -> bool:
        counter = set()
        
        for num in nums:
            if num not in counter:
                counter.add(num)
            else:
                return True
            
        return False

    def containsDuplicate_sort(self, nums: list) -> bool:
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        return False

# nums = [1,1,1,3,3,4,3,2,4,2]
# nums = [1,2,3,4]
nums = [1,2,3,1]
sol = Solution()
print(sol.containsDuplicate(nums))
