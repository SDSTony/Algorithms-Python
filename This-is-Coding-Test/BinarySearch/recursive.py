def binary_search(array, target, start, end):
    # 찾았는데 없는 경우
    if start > end:
        return None
    
    mid = (start + end) // 2

    # 찾은 경우 중간점 인덱스 반환 
    if array[mid] == target:
        return mid

    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)

    else:
        return binary_search(array, target, mid + 1, end)

data = [1, 3, 5, 7, 9]

print(binary_search(data, 3, 0, 4))
print(binary_search(data, 2, 0, 4))
