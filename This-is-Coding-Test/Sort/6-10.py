N = int(input())

data = []

for i in range(N):
    data.append(int(input()))

data = sorted(data, reverse=True)

for d in data:
    print(d, end=" ")