nums = [1, 2, 3, 4, 5, 6, 7, 8]
is_duplicate = False

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] == nums[j]:
            is_duplicate = True

print(is_duplicate)
