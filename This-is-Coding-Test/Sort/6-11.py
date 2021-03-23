N = int(input())

data = []

for i in range(N):
    data.append(tuple(input().split()))

def setting(d):
    return int(d[1])

data = sorted(data, key=setting)

for d in data:
    print(d[0], end=" ")

