class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # use UPI to analyse and solve 
        # U- return true if the a number occurs more than once else returm false
        # P- use the sorting method or hashset. use the sorting method. sort the numbers, loop through the sorted numbers and return true if the number occurs more than once
        # Implementation
        nums.sort()
        for i in range(1,len(nums)):
            if nums[i] == nums [i -1]:
                return True
        return False
        