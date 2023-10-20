### Bisect Left

Use Math.floor. To know how to compute logic, compare two numbers; since we are using Math.floor, we need to increment by one if target is greater than mid index.

```py
def bisect_left(nums, target):
    s = 0
    e = len(nums) - 1

    while s < e:
        mid = s + Math.floor((e-s) / 2)
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

Use Math.ceil.

```py
def bisect_right(nums, target):
    s = 0
    e = len(nums) - 1

    while s < e:
        mid = s + Math.ceil((e-s) / 2)
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
