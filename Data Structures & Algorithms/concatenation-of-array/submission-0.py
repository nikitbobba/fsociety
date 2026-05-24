class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []
        i = 0
        while i < (2*n):
            res.append(nums[i%n])
            i += 1
        return res

        