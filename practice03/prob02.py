# 문제2.
# range() 함수와 유사한 frange() 함수를 작성해 보세요. frange() 함수는 실수 리스트를 반환합니다

def frange(val, start=0.0, step=0.1):
    result = []
    i = start

    if val < start:
        i = val
        val = start

    while i < val:
        result.append(i)
        i += step

    return result


print(frange(2))
print(frange(1.0, 2.0))
print(frange(1.0, 3.0, 0.5))
