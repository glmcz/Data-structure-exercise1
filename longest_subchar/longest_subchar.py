
def length_of_longest_substring(s: str) -> int:
    longest = {}
    left = 0
    max_length = 0

    for index, c in enumerate(s):
        if c in longest and longest[c] >= left:
            left = max(left, longest[c] + 1)

        longest[c] = index
        max_length = max(max_length, index - left + 1)
    return max_length


if __name__ == '__main__':
    print(length_of_longest_substring("abcdeaar"))