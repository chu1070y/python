# 문제2. 키보드로 정수 수치를 입력 받아 짝수인지 홀수 인지 판별하는 코드를 작성하세요.

number = input('수를 입력하세요: ')

try:
    print( '짝수' if int(number) % 2 == 0 else '홀수')

except:
    print('정수가 아닙니다.')