class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sdict = dict()
        tdict = dict()

        for i in range(len(s)):
            sdict[s[i]] = sdict.get(s[i], 0) + 1
        
        for i in range(len(t)):
            tdict[t[i]] = tdict.get(t[i], 0) + 1
        return sdict == tdict

        