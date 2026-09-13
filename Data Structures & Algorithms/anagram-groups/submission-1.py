class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # get the ordered list of characters for all the values
        # store them in dictionary. If new entry, create new one
        # If a similar key exists then add it in the values
        
        # Time complexity: O(n*max(m))
        # Space complexity: O(n)

        anagrams = {}

        for str_ in strs:
            freq = [0]*26
            for char in str_:
                ordinal = ord(char) - ord("a")
                freq[ordinal] += 1
            freq_tuple = tuple(freq)
            
            if freq_tuple not in anagrams:
                anagrams[freq_tuple] = []
            
            anagrams[freq_tuple].append(str_)

        
        return list(anagrams.values())
        