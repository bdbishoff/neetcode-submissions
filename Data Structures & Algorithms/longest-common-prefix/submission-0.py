class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # string var res to keep track
        # for loop to go through each letter of each string
        # if any stray, then stop and return res as is

        res = ""
        i = 0
        while True:
            curr_l = None
            for word in strs:

                if len(word) - 1 < i:
                    return res

                if not curr_l:
                    curr_l = word[i]
                    continue
                
                if curr_l != word[i]:
                    return res

            res += curr_l
            i += 1
        
                

        