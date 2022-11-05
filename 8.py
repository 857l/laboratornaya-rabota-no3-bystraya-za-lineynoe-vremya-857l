import time, os, psutil
import math

t_start = time.perf_counter()

process = psutil.Process(os.getpid())

f = open('input.txt', 'r')


def partitioning(array, l, r, array2):
    pivot = r
    i = l - 1

    for j in range(l, r):
        if array[j] <= array[pivot]:
            i += 1

            array[i], array[j] = array[j], array[i]
            array2[i], array2[j] = array2[j], array2[i]

    array[i + 1], array[r] = array[r], array[i + 1]
    array2[i + 1], array2[r] = array2[r], array2[i + 1]
    return i + 1


def quicksort(array, l, r, array2):
    if l < r:
        pivot = partitioning(array, l, r, array2)
        quicksort(array, l, pivot - 1, array2)
        quicksort(array, pivot + 1, r, array2)


n = f.readline().split()
k = int(n[1])
n = int(n[0])

arr = []
distance = []

for i in range(n):
    a = (f.readline()).split()
    a[0] = int(a[0])
    a[1] = int(a[1])
    distance.append((math.sqrt(a[0]**2 + a[1]**2)))
    arr.append(a)

f = open('output.txt', 'w')

quicksort(distance, 0, len(distance) - 1, arr)

f.write(str(arr[:k]))
f.close()

print("Время работы: %s секунд " % (time.perf_counter() - t_start))
print(process.memory_info().rss / (1024 * 1024))
