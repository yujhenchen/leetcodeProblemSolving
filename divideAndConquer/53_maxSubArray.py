from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Return sum entire list if only one element
        # Loop to look at each element
        # Use tempSum to keep current accumulated max sum
        # If the newly added element make the current accumulated max sum smaller than 0,
        # reset current accumulated max sum to 0, and start from the element next to the newly added element

        if len(nums) == 1:
            return sum(nums)

        maxSum = nums[0]
        tempSum = 0
        for i in range(len(nums)):
            tempSum += nums[i]

            if tempSum > maxSum:
                maxSum = tempSum

            if tempSum < 0:
                tempSum = 0
        return maxSum
