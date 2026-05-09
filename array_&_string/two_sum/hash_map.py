# cari 2 angka dalam array
# jumlah kedua angka harus sama dengan target
# tidak boleh memakai index yang sama 2 kali
# hanya mencari 1 pasangan yang valid

nums = [3, 2, 4]
target = 6
mem = []

for i in nums:
    need = target - i

    if need in mem:
        print("ketemu:", need, i)

    mem.append(i)
