# 문제3. 다음과 같은 출력이 되도록 이중 for~in 문을 사용한 코드를 작성하세요.

for i in range(1, 11):
    for j in range(0, i):
        print("*", end='')
    print()