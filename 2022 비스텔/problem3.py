import sys
input = sys.stdin.readline

k = int(input())
estimates = list(map(int, input().split()))
n = len(estimates)
window = sum(estimates[:k])
answer = window

for i in range(k, n):
    window += estimates[i] - estimates[i-k]
    answer = max(answer, window)

print(answer)
