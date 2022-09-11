from my_minipack.progressbar import ft_progress
from my_minipack.logger import log
from time import sleep

if __name__ == '__main__':
    # listy = range(1000)
    # ret = 0
    # for elem in ft_progress(listy):
    #     ret += (elem + 3) % 5
    # sleep(0.05)
    # print()
    # print(ret)

    listy = range(3333)
    ret = 0
    for elem in ft_progress(listy):
        ret += elem
        sleep(0.005)
    print()
    print(ret)
