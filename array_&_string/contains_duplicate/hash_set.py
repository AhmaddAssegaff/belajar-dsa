nums = [1, 2, 3, 4, 5, 6, 7, 8, 1]
is_duplicate = False

seen = []

for num in nums:
    found = False

    for idx in seen:
        if idx == num:
            found = True

    if found:
        is_duplicate = True

    seen.append(num)

print(is_duplicate)
