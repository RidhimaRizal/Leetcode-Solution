# Problem: Intersection of Two Arrays
# LeetCode: https://leetcode.com/problems/intersection-of-two-arrays/
# Approach: Nested Loops
# Time Complexity: O(n*m + k^2)
# Space Complexity: O(k)
class Solution:
    def intersection(self, num1: list[int], num2: list[int]) -> list[int]:
        arr=[]
        for i in range(len(num1)):
            for j in range(len(num2)):
                if num1[i]==num2[j]:
                    if num1[i] not in arr:
                        arr.append(num1[i])
        return arr
        

 

