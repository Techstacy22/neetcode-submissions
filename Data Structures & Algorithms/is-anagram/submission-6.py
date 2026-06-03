class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #if they arent the same lenths they cant be anagrams 
        if len(s) != len(t):
            return False
        # dictionary to store the frequency count 
        count = {}
        #count each character in the first str s 
        #if it already exists add 1 else start the count from 1
        for char in s:
            count[char] = 1 + count.get(char, 0)
        #count each character in the str s and even not in count return false
        for char in t:
            if char not in count:
                return False
                 #remove one occurence 
            count[char] -= 1
            if count[char] < 0:
                return False
       
        return True





