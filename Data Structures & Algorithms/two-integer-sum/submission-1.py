class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d ={}
        for i in range(len(nums)):
            num = nums[i]
            n = target - num
            if n in d:
                return [d[n], i]
            d[num] = i