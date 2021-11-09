import time
import sys

def progress_bar(number):
    bar_lenght = 15
    filled_lenght = int(15 * number / 1000)
    bar = '=' * filled_lenght + '>'
    sys.stdout.write("[%s]" % bar)


def ft_progress(listy):
    number = 0
    start = time.time()
    for number in listy:
        number += 1
        yield number
        end = time.time()
        elapsed_time = end - start
        percentage = int(number / 10)
        eta = (1000 - number) / 100
        sys.stdout.write("ETA: %.2fs " % eta)
        sys.stdout.write("[ %d%%]" % percentage)
        progress_bar(number)
        sys.stdout.write(" %d/1000 | " % number)
        sys.stdout.write("elapsed time %.2fs\r" % elapsed_time)


listy = range(1000)
ret = 0
for elem in ft_progress(listy):
    ret += (elem + 3) % 5
    time.sleep(0.005)
print()
print(ret)
