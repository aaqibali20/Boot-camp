class Solution:
    def maxProduct(self, nums):
        curMax = curMin = ans = nums[0]

        for n in nums[1:]:
            temp = curMax

            curMax = max(n, n * curMax, n * curMin)
            curMin = min(n, n * temp, n * curMin)

            ans = max(ans, curMax)

        return ans 