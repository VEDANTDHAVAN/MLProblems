# Ransom Note

Beginner | dsa-sheet | hashing | counting-with-dictionaries

Return `True` if you can build the string `note` using letters cut from `magazine`, where each letter of the magazine can be used **at most once**. Otherwise return `False`.

### Examples

**Example 1**

Input:

```python
ransom_note('aab', 'baa')
```

Output:

```text
True
```

**Example 2**

Input:

```python
ransom_note('aa', 'ab')
```

Output:

```text
False
```

### Constraints

- `0 <= len(note), len(magazine) <= 3 * 10**5`
- Both strings contain lower-case letters.
