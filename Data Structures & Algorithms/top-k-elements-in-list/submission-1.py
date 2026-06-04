class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # sreate a dictionary 
        count = {}
        #loop through everynumber 
        for num in nums:
            #look for num i dictionary if found return its value 
            #else return 0then move to the next 
            count[num] = count.get(num, 0) + 1
        #sort the dictionary
        sorted_nums = sorted(
            count.items(),
            key=lambda item: item[1],
            reverse=True 
            )
        result = []
        for i in range(k):
            result.append(sorted_nums[i][0])
        return result 


        