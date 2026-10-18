# Problem: First Unique Character in a String
# LeetCode:  https://leetcode.com/problems/First-Unique-Character-in-a-String/
# Approach: Hashing
# Time Complexity: O(n)
# Space Complexity: O(1) for lower case characters
class Solution:
    def firstUniqChar(self, s):
        freq={}
        for i in s:
            if i not in freq:
                freq[i]=1
                
            else:
               freq[i]+=1
        for i in range(len(s)):
            if freq[s[i]]==1:
                return i
        return -1
