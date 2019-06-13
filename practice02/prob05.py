# 문제5.
# 함수 sum 을 만드세요. 이 함수는 임의의 개수의 인수를 받아서 그 합을 계산합니다.

def mysum(*num):
    sum = 0
    for n in num:
        sum += n
    return sum

print(mysum())
print(mysum(1, 2))
print(mysum(1, 3, 6, 8))

