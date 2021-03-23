"""
Time Complexity: O(N^2)
"""
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

N = len(array)

for i in range(1, N): # 아직 정렬 안된 부분
    for j in range(0, i): # 정렬 된 부분
        if array[j] > array[i]:
            temp = array[i]
            array[j+1:i+1] = array[j:i]
            array[j] = temp
            break

print(array)