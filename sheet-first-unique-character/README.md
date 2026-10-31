# First Unique Character

Beginner | dsa-sheet | hashing | counting-with-dictionaries

Return the **index** of the first character in `s` that appears **exactly once** in the whole string, or `-1` if every character repeats (or the string is empty).

### Examples

**Example 1**

Input:

```python
first_unique_character('leetcode')
```

Output:

```text
0
```

`l` at index 0 appears once.

**Example 2**

Input:

```python
first_unique_character('aabb')
```

Output:

```text
-1
```

Every character repeats.

### Constraints

- `0 <= len(s) <= 3 * 10**5`
- `s` contains lower-case letters.
