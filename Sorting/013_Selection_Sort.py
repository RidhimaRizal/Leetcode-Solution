# Problem: Selection Sort
# Approach: Selection Sort
# Time Complexity: O(n^2)
# Space Complexity: O(1)
class Solution:
    def Selection_sort(self,nums):
        n=len(nums)
        for i in range(n):
            minmum=nums[i]
            ind=i
            for j in range(i+1,n):
               if nums[j] < minmum:
                   minmum=nums[j]
                   ind=j
            nums[i],nums[ind]=nums[ind],nums[i]
        return nums
obj=Solution()
print(obj.Selection_sort([3,2,8,1,7,6,4]))
