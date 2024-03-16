import random
import time


def test():
    i = 0
    while i < 1000:
        ran = random.random()
        # print(ran)
        i =  i + 1
        time.sleep(1)


if __name__ == '__main__':
    test()
