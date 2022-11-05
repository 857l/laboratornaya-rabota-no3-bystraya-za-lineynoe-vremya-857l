import time, os, psutil

t_start = time.perf_counter()

process = psutil.Process(os.getpid())

f = open('input.txt', 'r')

def get_array(file):
    array = file.readline()
    array = array.split()
    for i in range(len(array)):
        array[i] = int(array[i])
    return array


def partitioning(array, l, r):
    pivot = r
    i = l - 1

    for j in range(l, r):
        if array[j] <= array[pivot]:
            i += 1

            array[i], array[j] = array[j], array[i]
    array[i + 1], array[r] = array[r], array[i + 1]
    return i + 1


def quicksort(array, l, r):
    if l < r:
        pivot = partitioning(array, l, r)
        quicksort(array, l, pivot - 1)
        quicksort(array, pivot + 1, r)


a = get_array(f)
quicksort(a, 0, len(a) - 1)

ans = 0

for i in range(len(a) - 1, -1, -1):
    if len(a) - i > a[i]:
        break
    ans = len(a) - i

f = open('output.txt', 'w')

f.write(str(ans))
f.close()

print("Время работы: %s секунд " % (time.perf_counter() - t_start))
print(process.memory_info().rss / (1024 * 1024))
