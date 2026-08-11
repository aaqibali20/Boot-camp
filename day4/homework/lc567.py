class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter

        n = len(s1)
        target = Counter(s1)
        window = Counter(s2[:n])

        if target == window:
            return True

        for i in range(n, len(s2)):
            window[s2[i]] += 1
            window[s2[i-n]] -= 1

            if window[s2[i-n]] == 0:
                del window[s2[i-n]]

            if window == target:
                return True

        return False