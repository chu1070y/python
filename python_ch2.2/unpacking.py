# packing : tuple만 가능하다

t = 10, 20, 30, 'python'
print(t, type(t))

# unpacking
a, b, c, d = t
print(a, b, c, d)

# 에러
# a, b, c = t
# a, b, c, d, e, f = t

# unpacking extended
t = (1, 2, 3, 4, 5)
a, *b = t
print(a, b, type(b))


# cf. 여러개 파라미터를 받는 함수
def mysum(*num):
    sum = 0
    for n in num:
        sum += n
    return sum


print(mysum(1, 2))
print(mysum(1, 2, 3))
print(mysum(1, 2, 3, 4, 5, 6))

print("*-+--*-*-**--")


# c의 printf() 함수흉내내기
def printf(str, *param):
    print(str % param)


printf("name: %s, age: %d", "둘리", 10)
# 결과
# name: 둘리, age: 10

