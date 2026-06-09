class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count_d = {}
        for i in range(len(s)):
            count_d[s[i]] = count_d.get(s[i], 0) + 1
            count_d[t[i]] = count_d.get(t[i], 0) - 1

        for v in count_d.values():
            if v != 0:
                return False

        return True