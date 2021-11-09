import time
import sys

def ft_progress(lst):
    n = 0
    start = time.time()
    for n in lst:
        n += 1
        yield n
        print(n)

listy = range(1000)
ret = 0
for elem in ft_progress(listy):
    ret += (elem + 3) % 5
    time.sleep(0.005)
print()
print(ret)
