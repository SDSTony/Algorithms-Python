N = int(input())
storage = list(map(int, input().split()))
M = int(input())
query = list(map(int, input().split()))

storage = sorted(storage)

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return mid

        elif array[mid] > target:
            end = mid - 1

        else:
            start = mid + 1

    return None

for q in query:
    result = binary_search(storage, q, 0, N - 1)
    if result != None:
        print('yes', end=' ')
    else:
        print('no', end=' ')
