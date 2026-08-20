class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # dictionary key of the string that points to a list to add it to? 
        d = defaultdict(list)
        print(ord("a"))

        for word in strs:
            key = [0] * 26
            for c in word:
                key[ord(c) - 97] += 1
            d[tuple(key)].append(word)
        return list(d.values())
    
        