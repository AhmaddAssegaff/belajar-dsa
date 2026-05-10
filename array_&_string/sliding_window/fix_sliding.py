nums = [4, 2, 1, 7, 8]
k = 3

window_sum = sum(nums[:k])

print("window_sum", window_sum)

for i in range(k, len(nums)):
    outgoing_num = nums[i - k]
    incoming_num = nums[k]

    window_sum = window_sum - outgoing_num + incoming_num

    print("window_sum", window_sum)
