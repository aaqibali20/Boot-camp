from typing import List
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        fmax = None
        smax = None
        tmax = None
        for num in nums:
            if num == fmax or num == smax or num == tmax:
                continue
            if (fmax == None or num > fmax):
                tmax = smax
                smax = fmax
                fmax = num
            elif(smax == None or num>smax):
                tmax = smax
                smax = num
            elif(tmax == None or num > tmax):
                tmax = num
        return fmax if tmax == None else tmax