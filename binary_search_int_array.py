from typing import List

def searchInsert(nums: List[int], target: int) -> int:
    # import ipdb
    # ipdb.set_trace()
    b = 0
    e = len(nums) - 1
    n = 0
    while b <= e:
        n = (b + e) // 2
        if target < nums[n]:
            e = n - 1
        elif target > nums[n]:
            b = n + 1
        else:
            return n

    if nums[n] < target:
        return n + 1
    else:
        return n


if __name__ == "__main__":
    l = [1,2,4,6,7]
    i = 3
    print(searchInsert(l, i))
