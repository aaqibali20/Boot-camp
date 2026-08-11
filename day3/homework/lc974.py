class Solution:
    def subarraysDivByK(self, nums, k):
        count = 0
        prefix = 0
        mp = {0: 1}

        for x in nums:
            prefix += x
            r = prefix % k

            if r in mp:
                count += mp[r]

            mp[r] = mp.get(r, 0) + 1

        return count