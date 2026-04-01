class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # so in the past we've sorted the word
        # then that sorted work maps to a dictionary key
        # where the value is an array and if the array
        # already exists then we just append through it
        # this solution is limited by the sorting alogirthm 
        # so max nlogn? 

        #math matical way to represent the string and then sort it based on that?
        d = defaultdict(list)
        
        for wrd in strs:
            k = [0] * 26
            for c in wrd:
                val = ord(c) - 97
                k[val] += 1
            d[tuple(k)].append(wrd)
            
        return list(d.values())

        