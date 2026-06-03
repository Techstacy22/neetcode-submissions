class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      #create a dictionary to store keys and thier values 
        dict = {}
        # loop through  nums
        for i in range(len(nums)):
            #where num is the value of key 
            num = nums[i]
            n = target - num  

            if n in dict:
                return [dict[n],i]
            dict[num] = i

