# cari 2 angka dalam array
# jumlah kedua angka harus sama dengan target
# tidak boleh memakai index yang sama 2 kali
# hanya mencari 1 pasangan yang valid

nums = [3, 2, 4]
target = 6

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        jumlah = nums[i] + nums[j]

        if jumlah == target:
            print("ketemu:", nums[i], nums[j])
