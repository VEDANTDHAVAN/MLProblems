def first_unique_character(s: str) -> int:
    freq = {}

    for char in s:
        freq[char] = freq.get(char, 0) + 1

    for i, ch in enumerate(s):
        if freq[ch] == 1:
            return i

    return -1
