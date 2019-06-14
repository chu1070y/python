def f():
    l_a = 2
    l_b = '마이콜'
    print(locals())


class MyClass:
    x = 10
    y = 20


g_a = 1
g_b = '둘리'
# print(globals())
# f()

# 1. 정의된 함수
f.k = 'hello'
# print(f.__dict__)

# 2. 클래스 객체
MyClass.z = 10
# print(MyClass.__dict__)


# 내장 함수
# 심벌 테이블 X -> 확장 x
# print.z = 10
# print(print.__dict__)

# 내장 클래스
# 심벌 테이블 O -> 확장  X
# str.z = 10
# print(str.__dict__)

# 내장클래스로 생성된 객체
# 심벌테이블 x -> 확장 x
# g_a.z = 10
# print(g_a.__dict__)

# 사용자 정의된 클래스로 생성된 객체
# 심벌테이블 o -> 확장 o
o = MyClass()
o.z = 10
print(o.__dict__)
