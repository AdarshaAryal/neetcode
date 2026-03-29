class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for str_ in strs:
            res += str(len(str_)) + "#" + str_
        return res 
    def decode(self, s: str) -> List[str]:
        i = 0
        res_lst = []
        while i < len(s):
            length = 0
            while i < len(s) and s[i].isdigit():
                length = length*10 + int(s[i])
                i += 1
            
            i += 1
            res_lst.append(s[i: i+length])
            i = i + length
            
        
        return res_lst
