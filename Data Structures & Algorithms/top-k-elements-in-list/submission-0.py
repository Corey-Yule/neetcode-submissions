class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        count = 0
        print(k)
        for j in nums:
            if j in seen:
                seen[j] = seen[j] + 1
            else:
                seen[j] = 1


        freq = sorted(seen, key=seen.get, reverse = True)


        print(freq)

        return freq[:k]