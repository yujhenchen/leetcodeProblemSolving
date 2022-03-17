class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # NOTE: the index is changed after element is removed from array
        # loop the array till next is the last element in the array, keep current one and the next one
        # if current == next, remove next, make next = next's next
        # else current = next, next = next's next

        currIndex = 0
        nextIndex = currIndex + 1
        while nextIndex < len(nums):
            if nums[currIndex] == nums[nextIndex]:
                nums.remove(nums[nextIndex])
            else:
                currIndex = nextIndex
            nextIndex = currIndex + 1
            # print(currIndex, nextIndex)
        # print(nums)
        return len(nums)
