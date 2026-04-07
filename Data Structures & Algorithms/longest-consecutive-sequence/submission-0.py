class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # this involves using a set
        # if n - 1 not in set
        # want to start at the end of the sequence
        # max counter as we go through each one
        s = set(nums)
        maxl = 0
        for n in nums:
            if n-1 in s:
                continue
            else:
                count = 1
                while (n+1) in s:
                    count += 1
                    n += 1
                maxl = max(maxl, count)
        return maxl



        