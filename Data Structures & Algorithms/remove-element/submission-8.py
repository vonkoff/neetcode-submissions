class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        counter = 0
        for i, num in enumerate(nums):
            if nums[i] != val:
                nums[counter] = nums[i]
                counter += 1
            else:
                k += 1
        return counter

