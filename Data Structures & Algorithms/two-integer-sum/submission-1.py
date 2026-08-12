class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #Target - x = y - Answer
        seen = {} # hashmap to lookup

        for index,num in enumerate(nums):
            find = target - num
            
            if find in seen:
                return [seen[find], index]
        
            seen[num] = index