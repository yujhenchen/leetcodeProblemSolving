from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # Get the middle element of the list
        # Start from index 0 to middle -1 if target is smaller than middle element
        # Start from middle + 1 to end if target is bigger than middle element

        if len(nums) == 1:
            if target > nums[0]:
                return 1
            else:
                return 0

        if target < nums[0]:
            return 0

        if target > nums[len(nums) - 1]:
            return len(nums)

        start = 0
        end = len(nums) - 1
        middle = (start + end) // 2
        while start <= end:
            if target == nums[middle]:
                return middle
            if target > nums[middle]:
                start = middle + 1
            if target < nums[middle]:
                end = middle - 1
            middle = (start + end) // 2

        if target > nums[start]:
            return start + 1
        else:
            return start
