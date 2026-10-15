# Problem: Two Sum with sorted Array
# LeetCode: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
# Approach: Two Pointers
# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def twoSum(self, numbers, target):
        left=0
        right=len(numbers)-1
        while left<right:
            ans=numbers[left]+numbers[right]
            if ans==target:
                return [left+1,right+1]
            elif ans>target:
                right-=1
            else:
                left+=1
                
