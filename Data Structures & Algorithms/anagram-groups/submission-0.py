class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a2w = collections.defaultdict(list)
        for str_ in strs:
            num_rep_str = [0]* 26
            for char in str_:
                char_idx = ord(char) - ord("a")
                num_rep_str[char_idx] += 1
            
            num_rep_key = tuple(num_rep_str)
            a2w[num_rep_key].append(str_)
    
        return list(a2w.values())

        