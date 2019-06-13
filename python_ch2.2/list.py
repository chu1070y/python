# 리스트 생성
l = [1, 2, 'python']

print(l, type(l))

# indexing
print(l[-3], l[-2], l[-1], l[0], l[1], l[2])

# slicing
print(l[1:3])
print(l[:])
print(l[2:])
print(l[len(l)-1::-1])

# 반복 (*)
l2 = l * 2
print(l2)

# 연결 (+)
l3 = l + [3,4,5]
print(l3)

# 길이
print(len(l3))

# 확인
print(5 in l3)

# 삭제
del l3[0]
print(l3)

# 변경가능한 시퀀스(mutable)
a = ['apple', 'banana', 10, 20]
a[2] = a[2] + 90
print(a)

# 슬라이싱을 통한 치환
a = [1, 12, 123, 1234]

a[0:2] = [10, 20]
print(a)

a[0:2] = [10]
print(a)

a[1:2] = [20]
print(a)

a[1:2] = []
print(a)

# 슬라이싱을 통한 삽입
a = [1, 12, 123, 234]

# 중간
a[1:1] = a[:]

# 위에 삽입
a.append(12345)
print()
