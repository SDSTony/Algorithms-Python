N = int(input())

d = [0] * 30002

d[2] = 1
d[3] = 1
d[5] = 1

for i in range(2, N+1):
    candidates = []
    if d[i] == 0:
        if i % 2 == 0:
            candidates.append(d[i // 2])

        if i % 3 == 0:
            candidates.append(d[i // 3])

        if i % 5 == 0:
            candidates.append(d[i // 5])

        candidates.append(d[i - 1])

        d[i] = min(candidates) + 1

print(d[N])