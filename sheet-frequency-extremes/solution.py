def frequency_extremes(nums: list[int]) -> list[int]:
    freq = {}

    for num in nums:
        freq[num] = freq.get(num, 0) + 1

    most = min(freq, key= lambda x: (-freq[x], x))

    least = min(freq, key= lambda x: (freq[x], x))

    return [most, least]
