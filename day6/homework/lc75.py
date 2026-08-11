class Solution:
    def sortColors(self, nums):
        n = len(nums)
        
        # Bubble Sort
        for i in range(n - 1):
            for j in range(n - i - 1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
class Solution:
    def sortColors(self, nums):
        low, mid, high = 0, 0, len(nums) - 1
        
        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
                
            elif nums[mid] == 1:
                mid += 1
                
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
