# Problem:Longest Substring Without Repeating Characters
# LeetCode: 03
# Approach: Sliding Window + Hashing (Set)
# Time Complexity: O(n)
# Space Complexity: O(min(n, charset))
class Solution:
    def lengthOfLongestSubstring(self,s):
        n=len(s)
        if n==0:
            return 0
        set1=set({})
        ans=1
        set1.add(s[0])
        i=0
        j=1
        while j<n:
            while s[j] in set1:
                set1.discard(s[i])
                i+=1
            set1.add(s[j])
            j+=1
            ans=max(ans,j-i)
        return ans 
obj=Solution()
print(obj.lengthOfLongestSubstring("abcabdabba"))
