count = 1
while count < 11:
    print(count, end=' ')
    count += 1
else:
    print()

# break, confinue, else문 적용

i = 0
while i < 10:
    i += 1

    if i < 5:
        continue

    if i >= 10:
        break

    print(i, end=' ')
else:
    print('ok')

# 무한루프
i = 0
while True:
    print(i, end=' ')
    if i > 5:
        break

    i += 1
else:
    print('else block')




