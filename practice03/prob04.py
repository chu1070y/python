# 문제4.
# 구구단 중에 특정 곱셈을 만들고 그 답을 선택하는 프로그램을 작성하는 문제입니다.
# 답을 포함하여 9개의 정수가 아래와 같은 형태로 출력되고 사용자는 답을 골라 입력하게 됩니다.
# 프로그램은 정답 여부를 다시 출력합니다.
import random

a = random.randint(1, 9)
b = random.randint(1, 9)
answer = a * b

print(a, 'x', b, '= ?')

select = [random.randint(1, 81) for x in range(9)]
select[random.randint(0, 8)] = answer

print()
for i in range(9):
    print(select[i], end='\t')

    if (i + 1) % 3 == 0:
        print()


check = int(input('answer: '))
[print("정답") if check == answer else print("오답")]