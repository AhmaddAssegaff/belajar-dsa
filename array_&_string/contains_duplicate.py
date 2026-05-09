nums = [1, 2, 3, 4, 5, 6, 7, 8, 1]
is_duplicate = False

# Brute force
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] == nums[j]:
            is_duplicate = True

# Hashset
seen = []

for num in nums:
    found = False

    for idx in seen:
        if idx == seen:
            found = True

    if found:
        is_duplicate = True

    seen.append(num)

print(is_duplicate)
