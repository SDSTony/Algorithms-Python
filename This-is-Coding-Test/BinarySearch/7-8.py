N, M = map(int, input().split())

ricecake = list(map(int, input().split()))

def calculate_leftover(ricecakes, H):
    total = 0
    for cake in ricecakes:
        leftover = cake - H
        if leftover > 0:
            total += leftover
    
    return total

def binary_search(array, M, start, end):

    while start <= end:
        H = (start + end) // 2
        leftovers = calculate_leftover(array, H)

        if leftovers == M:
            return H
        
        elif leftovers < M:
            end = H - 1

        else:
            start = H + 1

    return None

print(binary_search(ricecake, M, 0, max(ricecake)))