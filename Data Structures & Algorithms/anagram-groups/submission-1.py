class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
      #create a dictionary 
        groups = {}
    #loop through words
        for word in strs:
    # sort the words 
           sorted_words = "".join(sorted(word))
    # put into a dictionary
           if sorted_words not in groups:
               groups[sorted_words] = []
#add original word 
           groups[sorted_words].append(word)
        return list(groups.values())

