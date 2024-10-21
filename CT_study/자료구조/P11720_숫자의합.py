n = input()
numbers = list(input())
sum = 0

for i in numbers:
    sum = sum + int(i) # numbers에 있는 각 자리 수를 가져와 더하기

print(sum)