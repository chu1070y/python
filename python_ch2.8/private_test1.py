class cTest():
    __test_var = "private"

    def __init__(self):
        print("Create cTest")


# if __name__ == '__main__':
#     t1 = cTest()
#     print(t1.__test_var)


class cTest2():
    __test_var__ = "public"

    def __init__(self):
        print("Create cTest")

# if __name__ == '__main__':
#     t2 = cTest2()
#     print(t2.__test_var__)


class cTest3():
    __test_var__ = "public"

    def __init__(self):
        print("Create cTest")

    def __test(self):
        print('test')


if __name__ == '__main__':
    t3 = cTest3()
    print(t3.__test())
