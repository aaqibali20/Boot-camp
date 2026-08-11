from typing import List 

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)

        while l < r:
            mid = (l + r) // 2
            d = 1
            total = 0

            for w in weights:
                if total + w > mid:
                    d += 1
                    total = 0
                total += w

            if d <= days:
                r = mid
            else:
                l = mid + 1

        return l