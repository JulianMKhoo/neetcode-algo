class Solution:

    def encode(self, strs: List[str]) -> str:
        encode_str = ""
        for s in strs:
            n = len(s)
            encode_str += f"{n}#" + s
        return encode_str
    def decode(self, s: str) -> List[str]:
        start = 0
        end = 0
        n = len(s)
        decode_str = []
        while end < n:
            if s[end] == "#":
                new_pointer = int(s[start:end]) + end
                decode_str.append(s[end + 1:new_pointer + 1])
                end = new_pointer + (end - start)
                start = new_pointer + 1
                continue
            end+=1
        return decode_str