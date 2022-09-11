from time import sleep, time
import os


def ft_progress(lst):
    lst_len = len(lst)
    bar_width = 60
    start_time = time()
    for i, element in enumerate(lst):
        os.system('clear')
        elapsed_time = time() - start_time
        if i > 0:
            eta = (lst_len - i) * (elapsed_time / i)
        else:
            eta = float('inf')
        progress = int((i * bar_width) / lst_len)
        percentage = i * 100 / lst_len
        bar = '>'.rjust(progress + 1, '=').ljust(bar_width)
        print(f'ETA: {eta:.2f}s [{int(percentage):2}%] [{bar}] {i + 1}/{lst_len} | elapsed time {elapsed_time:.2f}')
        yield element


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
