from unicodedata import numeric


class Solution:

    def encode(self, strs: list[str]) -> str:
        # if len(strs) == 0:
        #     return
        output:str = ""
        delimiter = '#'
        for word in strs:
            word_lenght = len(word) # without -1 because of delimiter
            output += f"{word_lenght}{delimiter}{word}"
        return  output

    def decode(self, s: str) -> list[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1

            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j

    def decode_old(self, s: str) -> list[str]:
        output: list = []
        word_length = 0
        skip_delimiter = False
        word = ""
        str_number:str = ""
        for index, char in enumerate(s):
            if char >= '0' and char <= '9':
                str_number += char
                if int(str_number) == 0:
                    output.append("")
                    continue
                skip_delimiter = True
                continue


            if skip_delimiter:
                skip_delimiter = False
                word_length = int(str_number)
                str_number = ""
                continue

            if word_length != 0:
                word += char
                word_length -= 1

            if word and word_length == 0:
                output.append(word)
                word = ""

        return output

if __name__ == "__main__":
    strs = ["1,23","45,6","7,8,9"]
    encode = Solution().encode(strs)
    print("Output for encode is:\n")
    print(encode)
    print("Output for decode is:\n")
    print(Solution().decode(encode))