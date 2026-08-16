class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        l = sorted(set(nums))
        longest,current = 1,1

        print(l)
        for i in range(len(l) - 1):
            if l[i + 1] == l[i] + 1:
                current += 1
            else:
                longest = max(longest, current)
                current = 1
        return max(longest,current)