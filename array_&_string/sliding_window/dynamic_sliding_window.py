word = "pwwkew"

left = 0
right = len(word) - 1

seen = []
count_repeated_letters = 0

for right in range(len(word)):
    while word[right] in seen:
        seen.remove(word[left])
        left += 1

    seen.append(word[right])

    count_repeated_letters = max(count_repeated_letters, right - left + 1)

print(count_repeated_letters)
