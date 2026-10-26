# Approach: Insertation Sort
# Time complexity: Best-case time complexity: O(n)
#                   Average-case time complexity: O(n^2)
#                   Worst-case time complexity: O(n^2)
# Space Complexity: O(n)

class Solution:
    def insertation_sort(self,nums):
        n=len(nums)
        for i in range(1,n):
            key=nums[i]
            j=i-1
            while j>=0 and nums[j]>key:
                nums[j+1]=nums[j]
                j-=1
            nums[j+1]=key
        return nums
obj=Solution()
print(obj.insertation_sort([3,2,8,1,7,6,4]))
