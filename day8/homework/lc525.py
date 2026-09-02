from typing import List 
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count = 0
        first = {0: -1}
        ans = 0

        for i, num in enumerate(nums):
            if num == 0:
                count -= 1
            else:
                count += 1

            if count in first:
                ans = max(ans, i - first[count])
            else:
                first[count] = i

        return ans