import sys


def func():
    count = int(sys.argv[1])
    for i in range(1, count + 1):
        print(' ' * (count - i), '#' * i, sep='')


if __name__ == '__main__':
    func()
