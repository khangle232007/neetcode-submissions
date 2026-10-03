class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for i in range(len(strs)):
            length = str(len(strs[i]))
            new_strs = length + "#" + strs[i]
            s += new_strs
        return s
        
    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            word = ""
            word_length = ""
            while s[i].isnumeric():
                word_length += s[i]
                i += 1
            word_length = int(word_length)
            #skip the "#"
            i += 1
            for j in range(word_length):
                word += s[i + j]
            i += word_length
            result.append(word)         
        return result

