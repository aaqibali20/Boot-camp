from typing import List
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        count = {}
        curr = 0
        ans = 0

        for i in range(len(nums)):
            count[nums[i]] = count.get(nums[i], 0) + 1
            curr += nums[i]

            if i >= k:
                count[nums[i - k]] -= 1
                if count[nums[i - k]] == 0:
                    del count[nums[i - k]]
                curr -= nums[i - k]

            if i >= k - 1 and len(count) == k:
                ans = max(ans, curr)

        return ans