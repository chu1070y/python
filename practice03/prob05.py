# 문제5.
# 선택정렬(제자리 정렬 알고리즘)을 적용하는 코드를 완성하세요.
# 문제에 주어진 배열 [ 5, 9, 3, 8, 60, 20, 1 ] 를 크기 순서대로 정렬하여
# 다음과 같은 출력이 되도록 완성하는 문제입니다.
#
# << 출력 결과 >>
#
# Before sort.
# 5 9 3 8 60 20 1
# After Sort.
# 60 20 9 8 5 3 1.

arr = [5, 9, 3, 8, 60, 20, 1]

print('Before sort')
[print(x, end=' ') for x in arr]

print()
for i in range(len(arr) - 1):
    change = 0
    for j in range(0, len(arr) - 1):
        if arr[j] >= arr[j + 1]:
            continue

        temp = arr[j]
        arr[j] = arr[j + 1]
        arr[j + 1] = temp
        change += 1

    if change == 0:
        break;

print('After sort')
[print(x, end=' ') for x in arr]
