class Solution:
    def subarraySum(self, nums, k):
        count = 0
        prefix = 0
        mp = {0: 1}

        for x in nums:
            prefix += x

            if prefix - k in mp:
                count += mp[prefix - k]

            mp[prefix] = mp.get(prefix, 0) + 1

        return count