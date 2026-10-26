class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sChar, tChar = {}, {}

        for i in range(len(s)):
            sChar[s[i]] = 1 + sChar.get(s[i], 0)
            tChar[t[i]] = 1 + tChar.get(t[i], 0)
        return sChar == tChar