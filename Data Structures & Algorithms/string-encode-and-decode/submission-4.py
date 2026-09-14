class Solution:

    def encode(self, strs: List[str]) -> str:
        SEPARATOR = "#"
        res = []
        for str_ in strs:
            res.append(str(len(str_)) + SEPARATOR + str_)
        res = "".join(res)
        return res
    def decode(self, s: str) -> List[str]:
        res = []
        idx = 0

        while idx < len(s):
            cur_num = 0
            while s[idx].isdigit():
                cur_num = cur_num * 10 + int(s[idx])
                idx += 1
                if s[idx] == "#":
                    break
            
            idx += 1
            cur_string = s[idx:idx+cur_num]
            res.append(cur_string)
            idx += cur_num


        return res