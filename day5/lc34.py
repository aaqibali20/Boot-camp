class Solution:
    def searchRange(self, nums, target):
        def find(first):
            l, r = 0, len(nums) - 1
            ans = -1

            while l <= r:
                mid = (l + r) // 2

                if nums[mid] == target:
                    ans = mid
                    if first:
                        r = mid - 1
                    else:
                        l = mid + 1
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1

            return ans

        return [find(True), find(False)]