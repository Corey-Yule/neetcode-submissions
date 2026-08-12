class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l = n*2
        ans = list(range(l))
        
        for i in range(n):
            ans[i] = nums[i]
            ans[i+n] = nums[i]
        
        return ans