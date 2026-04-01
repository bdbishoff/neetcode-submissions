class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += f"{len(s)}#{s}"
        return res
                
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            num = ""
            while s[i] != "#":
                num += s[i]
                i += 1
            i += 1
            if num.isnumeric():
                res.append(s[i:i+int(num)])
                i += int(num)-1
            i += 1
        return res
        

