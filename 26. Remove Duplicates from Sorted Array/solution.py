class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        length = len(nums)
        while i < length - 1:
            if nums[i] == nums[i+1]:
                del nums[i+1]
                length -= 1
            else:
                i += 1
        return length