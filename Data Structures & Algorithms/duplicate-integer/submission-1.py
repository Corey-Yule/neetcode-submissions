class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for x in nums:  # x is the number itself
            if x in hashset:
                return True
            else:
                hashset.add(x)
        return False
