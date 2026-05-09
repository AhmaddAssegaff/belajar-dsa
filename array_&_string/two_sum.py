# cari 2 angka dalam array
# jumlah kedua angka harus sama dengan target
# tidak boleh memakai index yang sama 2 kali
# hanya mencari 1 pasangan yang valid

nums = [3, 2, 4]
target = 6

# Brute Force O(n)
for i in range(len(nums)):
    print(i, "I")
    for j in range(i + 1, len(nums)):
        print(j, "J")

        jumlah = nums[i] + nums[j]
        print("jumlah", jumlah)

        if jumlah == target:
            print(nums[i], nums[j])


# HashMap O(1)
mem = []

for i in nums:
    need = target - i

    if need in mem:
        print("ketemu:", need, i)

    mem.append(i)
