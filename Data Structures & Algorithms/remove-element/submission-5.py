class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0

        # go through the array, 
        # everytime we come accorss an 
        # grab curr element
        # if it equals the val
        # then turn it into _
        # start from the back of the array until we aren't at a _
        # place it there

        # go through once and replace everything with _
        # go through again moving each _ to the very back 
        i = 0

        while i < len(nums):
            print(nums)
            if nums[i] == val:
                k += 1
                # start replacement loop
                j = -1
                while nums[j] == "_":
                    j -= 1
                
                # swap j with i
                tmp = "_"
                nums[i] = nums[j]
                nums[j] = tmp
            else:
                i += 1

            
        return len(nums) - k