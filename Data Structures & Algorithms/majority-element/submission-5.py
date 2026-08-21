class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # the trick is the count up or down
        count = 1
        curr = nums[0]

        for i in range(1, len(nums)):
            if count == 0:
                curr = nums[i]
                count += 1
                continue

            if nums[i] == curr:
                count += 1
            else:
                count -= 1
        return curr

        