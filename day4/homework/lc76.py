class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter

        need = Counter(t)
        left = count = 0
        ans = ""

        for right, ch in enumerate(s):
            if ch in need:
                need[ch] -= 1
                if need[ch] >= 0:
                    count += 1

            while count == len(t):
                if not ans or right - left + 1 < len(ans):
                    ans = s[left:right + 1]

                if s[left] in need:
                    need[s[left]] += 1
                    if need[s[left]] > 0:
                        count -= 1

                left += 1

        return ans