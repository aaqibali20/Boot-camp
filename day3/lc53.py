class Solution:
    def maxSubArray(self, nums):
        max_sum = nums[0]
        sum = 0

        for v in nums:
            sum += v
            
            max_sum = max(max_sum, sum)
            
            if sum < 0:
                sum = 0
                
        return max_sum
