n = input()
score = list(map(int, input().split()))
mymax = max(score)
sum = sum(score)

print(sum * 100 / mymax / int(n))