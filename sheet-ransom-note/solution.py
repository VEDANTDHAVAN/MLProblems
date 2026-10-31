def ransom_note(note: str, magazine: str) -> bool:
    freq = {}

    for ch in magazine:
        freq[ch] = freq.get(ch, 0) + 1

    for ch in note:
        if freq.get(ch, 0) == 0:
            return False

        freq[ch] -= 1

    return True
