# 1. Local
# 2. Enclosing
# 3. Global
# 4. Bulit-in


a = 1  # G


def f():  # G
    b = 200  # E

    def g():
        # b = 100  # L
        print(b)
        print(__name__)

    g()


if __name__ == '__main__':
    f()
