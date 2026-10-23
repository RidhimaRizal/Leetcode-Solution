# problem: Sort in ascending order
# Approach: Bubble sort
# Time complexity: # Best Case: O(n),Average Case: O(n^2),Worst Case: O(n^2)
# space complexity: O(1)

class Solution:
    def bubble_sort(self,nums):
        n=len(nums)
        for i in range(n):
            isSwap=False
            for j in range(n-i-1):
                if nums[j]>nums[j+1]:
                    nums[j],nums[j+1]=nums[j+1],nums[j]
                    isSwap=True
            if not isSwap:
                break
        return nums 
obj=Solution()
print(obj.bubble_sort([3,2,8,1,7,6,4]))
