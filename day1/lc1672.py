from typing import List
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxi = 0

        for customer in accounts:
            curr = 0
            for money in customer:
                curr += money
            maxi = max(curr, maxi)
        return maxi