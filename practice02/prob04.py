# 문제4
# 반복문을 이용하여 369게임에서 박수를 쳐야 하는 경우의 수를 순서대로 화면에
# 출력해보세요. 1부터 99까지만 실행하세요.

# for data in range(1, 100):
#     count = 0
#
#     if data // 10 != 0 and data // 10 % 3 == 0:
#         count += 1
#
#     if data % 10 != 0 and data % 10 % 3 == 0:
#         count += 1
#
#     if count == 0:
#         continue
#
#     print(data, "짝" * count)

compare = {'3', '6', '9'}

for data in range(1, 100):
    data = str(data)

    count = sum([x in compare for x in data])

    if count:
        print(data, "짝" * count)