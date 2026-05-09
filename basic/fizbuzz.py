# jika angka habis dibagi 3 : print "Fizz"
# jika angka habis dibagi 5 : print "Buzz"
# jika angka habis dibagi 3 dan 5 : print "FizzBuzz"
# selain itu → cetak angkanya

num_range = 15

for i in range(1, num_range + 1):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
