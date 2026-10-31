# Most and Least Frequent Value

Beginner | dsa-sheet | hashing | counting-with-dictionaries

Return `[most, least]`: the value that appears **most often** and the value that appears **least often** in `nums`. If several values tie, take the **smaller value**.

### Examples

**Example 1**

Input:

```python
frequency_extremes([4, 4, 5, 5, 6])
```

Output:

```text
[4, 6]
```

`4` and `5` both appear twice; the smaller is 4. `6` appears once.

**Example 2**

Input:

```python
frequency_extremes([7])
```

Output:

```text
[7, 7]
```

One value is both the most and the least frequent.

### Constraints

- `1 <= len(nums) <= 3 * 10**5`
- `-10**9 <= nums[i] <= 10**9`
