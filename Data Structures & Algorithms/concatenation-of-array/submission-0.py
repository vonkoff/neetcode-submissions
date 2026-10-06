class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums) 
        ans = [None] * n * 2
    
        for pos in range(len(nums)):
            ans[pos] = nums[pos]
            print(pos + n)
            ans[pos + n] = nums[pos]
        return ans
            

        