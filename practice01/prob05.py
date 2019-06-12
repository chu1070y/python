# 문제5.
# 주어진 리스트 데이터를 이용하여 3의 배수의 개수와 배수의 합을 구하여 출력형태와 같이 출력하세요.


data = [x for x in range(1,50)]

print('주어진 리스트에서 3의 배수의 개수=>', len([x for x in data if x % 3 == 0]))
print('주어진 리스트에서 3의 배수의 합=>', sum([x for x in data if x % 3 == 0]))
