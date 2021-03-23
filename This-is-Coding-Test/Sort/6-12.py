N, K = map(int, input().split())

A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())), reverse=True)

for i in range(K):
    if A[i] < B[i]:
        A[i], B[i] = B[i], A[i]
    else: # 한번 크기가 역전되면, 그 이후로는 계속 역전 될 것이기 때문
        break

print(sum(A))