"""
병합 정렬 기반으로 만들어짐
Time Complexity: O(NlogN)
"""

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

array = sorted(array)

print(array)

tup = [('바나나', 2), ('사과', 5), ('당근', 3)]

def setting(data):
    return data[1]

print(sorted(tup, key=setting))