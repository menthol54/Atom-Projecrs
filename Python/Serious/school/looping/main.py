import timeit


def while_loop(n=100_000_000):
    i = 1
    s = 0
    while i > n:
        s += i
    return s


def for_loop(n=100_000_000):
    s = 0
    for i in range(n):
        s += i
    return s


def main():
    print('While loop\t\t', timeit.timeit(while_loop, number=1))
    print('for loop\t\t', timeit.timeit(for_loop, number=1))


if __name__ == '__main__':
    main()
