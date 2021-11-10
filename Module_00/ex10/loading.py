import time
import sys


def progress_bar(number, max_lst):
    bar_lenght = 15
    filled_lenght = int(15 * number / max_lst)
    bar = '=' * (filled_lenght) + '>' + ' ' * (bar_lenght - filled_lenght)
    sys.stdout.write("[%s]" % bar)


def ft_progress(listy):
    number = 0
    start = time.time()
    max_lst = max(listy) + 1
    for number in listy:
        number += 1
        yield number
        end = time.time()
        elapsed_time = end - start
        percentage = int(number / 10)
        eta = abs(elapsed_time / number * (max_lst - number))
        sys.stdout.write("ETA: %.2fs " % eta)
        sys.stdout.write("[ %d%%]" % percentage)
        progress_bar(number, max_lst)
        sys.stdout.write(" %d/%d | " % (number, max_lst))
        sys.stdout.write("elapsed time %.2fs\r" % elapsed_time)


listy = range(1000)
ret = 0
for elem in ft_progress(listy):
    ret += (elem + 3) % 5
    time.sleep(0.005)
print()
print(ret)
