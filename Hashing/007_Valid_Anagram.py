# Problem: Valid Anagram
# LeetCode: 242
# Approach: Hashing 
# Time Complexity: O(n)
# Space Complexity: O(k), where k is the number of unique characters
class Solution:
    def isAnagram(self, s, t):3
        freq={}
        if len(s)!=len(t):
            return False
        for i in s :
            if i not in freq:
                freq[i]=1
            else:
                freq[i]+=1
        for i in t :
            if i not in freq:
                return False
            else:
                freq[i]-=1
        for i in freq.values():
            if i!=0:
                return False
        return True
