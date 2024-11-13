word = input()
stack = []

for char in word:
    if stack and stack[-1] == char:
        stack.pop()
    else:
        stack.append(char)

if not stack:
    print("0")
else:
    print("1")