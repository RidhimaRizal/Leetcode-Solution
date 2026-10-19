# Problem: Substrings of Size Three with Distinct Characters
# LeetCode: 1876
# Approach: Sliding Window
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        n=len(s)
        ans=0
        for i in range(0,n-2):
            if s[i]!=s[i+1] and s[i+1]!=s[i+2] and s[i+2]!=s[i]:
                ans+=1
        return ans 
