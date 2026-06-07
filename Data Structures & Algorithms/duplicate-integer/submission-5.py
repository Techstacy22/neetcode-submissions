class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
      #use a hash set to store the numbers you have seen 
        seen = set()
        #loop  through every number in nums
        for num in nums:
            # if numis in seen return True 
            if num in seen:
                return True 
            seen.add(num)
        return False


        