class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for i in strs:
            encoded_string += str(len(i)) + "#" + i
        return encoded_string
    


    def decode(self, s: str) -> List[str]:
        decoded_string = []
        left, right = 0, 0
        while left < len(s):
            while s[right] != "#":
                right += 1
            length = int(s[left:right])
            left = right + 1
            right += length + 1
            decoded_string.append(s[left:right])
            left = right
        return decoded_string