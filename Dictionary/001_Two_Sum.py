# Problem: Two Sum
# LeetCode: https://leetcode.com/problems/two-sum/
# Approach: Hash Map
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        n=len(nums)
        dict1={}
      
        for i in range(n):
            rem=target-nums[i]
          
            if rem in dict1:
                return [dict1[rem],i]  
            else:
                dict1[nums[i]]=i
