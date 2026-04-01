class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sdict = dict()
        tdict = dict()
        for c in s:
            sdict[c] = sdict.get(c, 0) + 1

        for c in t:
            tdict[c] = tdict.get(c, 0) + 1
        return sdict == tdict

        