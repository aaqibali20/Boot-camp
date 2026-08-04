from typing import List
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        runningSum = []
        i = 0
        sums = 0
        for i in nums:
            sums =sums + i
            runningSum.append(sums)
        return runningSum