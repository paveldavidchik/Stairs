import sys


def func():
    count = int(sys.argv[1])
    step = 1
    for i in range(count):
        print(' ' * (count - step), '#' * step, sep='')
        step += 1


if __name__ == '__main__':
    func()
