import time


def demo1():
    """
     如果a+b+c=1000,且a^2+b^2=c^2(a,b,c是自然数)，求a,b,c
    @return:
    """
    start_time = time.time()
    for a in range(0, 1001):
        for b in range(0, 1001):
            for c in range(0, 1001):
                if a + b + c == 1000 and a ** 2 + b ** 2 == c ** 2:
                    print('a,b,c:{},{},{}'.format(a, b, c))
    end_time = time.time()
    print('times:{}'.format(end_time - start_time))
    print('finished')


def demo2():
    """
     如果a+b+c=1000,且a^2+b^2=c^2(a,b,c是自然数)，求a,b,c--->修改算法
    @return:
    """
    start_time = time.time()
    for a in range(0, 1001):
        for b in range(0, 1001):
            c = 1000 - a - b
            if a ** 2 + b ** 2 == c ** 2:
                print('a,b,c:{},{},{}'.format(a, b, c))
    end_time = time.time()
    print('times:{}'.format(end_time - start_time))
    print('finished')


if __name__ == '__main__':
    # demo1()
    demo2()
