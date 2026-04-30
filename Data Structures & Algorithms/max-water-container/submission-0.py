class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # identify: Two pointer
        # move two pointers towards the middle and keep track of the highest amount
        l,r = 0, len(heights) - 1
        res = 0

        while l < r:
            print(r, l, r-l, min(heights[l], heights[r]), (r-l) * min(heights[l], heights[r]))
            res = max((r-l) * min(heights[l], heights[r]), res)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return res


        