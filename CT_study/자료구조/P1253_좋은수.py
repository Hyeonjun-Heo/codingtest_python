import sys

input = sys.stdin.readline

N = int(input())
Result = 0
A = list(map(int, input().split()))
A.sort()

for k in range(N):
    find = A[k]
    i = 0
    j = N - 1
    while i < j:  # 투 포인터 알고리즘
        if A[i] + A[j] == find:  # find는 서로 다른 두 수의 합이어야 함을 체크
            if i != k and j != k:
                Result += 1
                break
        elif A[i] + A[j] < find:
            i += 1
        else:
            j -= 1
print(Result)

