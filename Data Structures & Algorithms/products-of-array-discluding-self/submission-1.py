class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # brute force
        # go through each option and keep a sum
        prefix = [nums[0]]
        postfix =[nums[-1]]

        precurr = nums[0]
        poscurr = nums[-1]
        for i in range(1, len(nums)):
            precurr *= nums[i]
            prefix.append(precurr)

            poscurr *= nums[-i - 1]
            postfix.append(poscurr)
        postfix.reverse()
        print(prefix, postfix)

        output = []
        for i in range(len(nums)):
            pre = 1
            po = 1
            if i-1 >= 0:
                pre = prefix[i-1]

            if i + 1 < len(nums):
                po = postfix[i+1]
            output.append(po * pre)
        return output
            



        
        
        