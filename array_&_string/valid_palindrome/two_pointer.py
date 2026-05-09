# kata/kalimat yang dibaca dari depan dan belakang tetap sama
# bandingkan karakter dari kiri dan kanan
# jika semua sama maka palindrome
# jika ada yang berbeda maka bukan palindrome

s = "A man a plan a canal Panama madam"
word = s.replace(" ", "").lower()

is_palindrome = True

left = 0
right = len(word) - 1

while left < right:
    print(word[left], word[right])

    left += 1
    right -= 1

    if word[left] != word[right]:
        is_palindrome = False


print(is_palindrome)
