## ini adalah soal pertama interview


# jawaban saya pribadi ketika interview User
def howManyGames(p, d, m, s):
    def kurangin(a, b):
        return a - b

    simpan = []
    berapa_kali_main = 0
    buget = s
    disc = d
    peak = p

    simpan.append(p)
    simpan_idx_terakhir = simpan[0::]

    minimal_harga = m

    while simpan_idx_terakhir - disc >= minimal_harga:
        hasil = kurangin(peak, disc)
        berapa_kali_main += 1
        simpan.append(hasil)

        if sum(simpan) == buget:
            return berapa_kali_main


howManyGames(20, 3, 6, 85)

# SOAL INTERVIEW — Halloween Sale / How Many Games
#
# Deskripsi Soal:
# Sebuah toko game sedang mengadakan diskon.
#
# - Harga game pertama adalah p
# - Setiap membeli game, harga game berikutnya turun sebesar d
# - Harga game tidak boleh turun di bawah m
# - Kamu memiliki budget sebesar s
#
# Tugas:
# Hitung berapa banyak game yang bisa dibeli.
#
# Contoh:
#
# p = 20
# d = 3
# m = 6
# s = 85
#
# Urutan harga game:
#
# 20
# 17
# 14
# 11
# 8
# 6
# 6
# ...
#
# Perhatikan:
# Setelah harga mencapai 6,
# harga tidak boleh turun lagi.
#
# Simulasi pembelian:
#
# Budget awal = 85
#
# 85 - 20 = 65
# 65 - 17 = 48
# 48 - 14 = 34
# 34 - 11 = 23
# 23 - 8  = 15
# 15 - 6  = 9
# 9  - 6  = 3
#
# Budget tersisa 3,
# tidak cukup membeli game lagi.
#
# Jawaban:
# 7 game
#
# PENDEKATAN YANG BIASANYA DIGUNAKAN
#
# 1. Mulai dari harga awal
# 2. Selama budget masih cukup:
#     - beli game
#     - kurangi budget
#     - tambah jumlah game
#     - turunkan harga
# 3. Jika harga sudah lebih kecil dari minimum:
#     - gunakan harga minimum terus
#
# COMPLEXITY
#
# Time Complexity:
# O(n)
# n = jumlah game yang berhasil dibeli
#
# Space Complexity:
# O(1)
#
# KESALAHAN PADA SOLUSI PERTAMA
#
# 1. simpan_idx_terakhir berisi LIST
#    bukan angka terakhir.
#
#    simpan[0::]
#    menghasilkan copy list.
#
# 2. Tidak pernah update harga terbaru
#    sehingga loop tidak berjalan benar.
#
# 3. Mengecek:
#    sum(simpan) == budget
#
#    padahal seharusnya:
#    total harga <= budget
#
# 4. Tidak menangani kondisi
#    ketika harga mencapai minimum.
#
# SOLUSI YANG BENAR
#
#
# def howManyGames(p, d, m, s):
#     harga = p
#     jumlah_game = 0
#     budget = s
#
#     while budget >= harga:
#         budget -= harga
#         jumlah_game += 1
#
#         # harga tidak boleh lebih kecil dari minimum
#         harga = max(m, harga - d)
#
#     return jumlah_game
#
#
# print(howManyGames(20, 3, 6, 85))
