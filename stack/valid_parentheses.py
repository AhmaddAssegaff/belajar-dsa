# LIFO Last In First Out
# insert method = PUSH
# delete method = POP

data = []
text = "((()))"
is_valid = True


def push(a):
    data.append(a)


def pop():
    if len(data) > 0:
        data.pop()


def top():
    return data[-1]


def empty():
    return len(data) == 0


for char in text:
    if char == "(" or char == "[" or char == "{":
        push(char)
        # print(data)

    if char == ")" or char == "]" or char == "}":
        pop()
        # print(data)

if empty() and is_valid:
    print("VALID")
else:
    print("INVALID")
