### Bisect Left

```py
def bisect_left(nums, target):
    s = 0
    e = len(nums) - 1

    while s < e:
        mid = s + ((e-s) // 2)
        if nums[mid] < target:
            s = mid + 1
        else:
            e = mid

        if nums[s] == nums[e]:
            if nums[s] == target:
                return s
            else:
                return -1

    if nums[s] == target:
        return s
    return -1
```

### Bisect Right

```py
def bisect_right(nums, target):
    s = 0
    e = len(nums) - 1

    while s < e:
        mid = s + ceil((e-s) / 2)
        if nums[mid] <= target:
            s = mid
        else:
            e = mid - 1

        if nums[s] == nums[e]:
            if nums[e] == target:
                return e
            else:
                return -1

    if nums[e] == target:
        return e
    return -1
```
