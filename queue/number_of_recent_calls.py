# mencari jumlah request dalam 3000 ms terakhir
# queue menyimpan request yang masih valid
# jika request terlalu lama maka dihapus dari depan

# contoh:
# ping(1)
# ping(100)
# ping(3001)
# ping(3002)

# saat ping(3002):
# range valid = [2 sampai 3002]
# maka request 1 dihapus karena sudah terlalu lama

# enqueue = masuk di array paling akhir
# dequeue = keluarin di array paling depan / yg pertama masuk
# FIFO = first in first out

data = []
t = 5000


def enqueue(a):
    data.append(a)


def dequeue():
    if len(data) > 0:
        data.pop(0)


def ping(t):
    enqueue(t)

    while data[0] < t - 3000:
        dequeue()

    return len(data)


print(ping(1))
print(ping(100))
print(ping(3001))
print(ping(3002))
print(ping(6002))
print(ping(9002))

print(data)
