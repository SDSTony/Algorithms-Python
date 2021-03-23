"""
Time Complexity: O(N^2)

거의 정렬된 상태일 경우, 최선의 경우 O(N)
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



# for i in range(1, len(array)):
#     for j in range(i, 0, -1):
#         if array[j] < array[j-1]:
#             array[j], array[j-1] = array[j-1], array[j]
#         else:
#             break