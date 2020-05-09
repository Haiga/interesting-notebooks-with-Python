import time
import threading

num = 100000000
# num = 10000000

start = time.time()


def thread_function(arr, pos1, pos2):
    new_range = range(pos1, pos2)
    for _ in new_range:
        x = (1 / 2) + 0.0000005 + 326.15
        arr[pos1] = x
        pos1 += 1


m_threads = []

my_range = range(num)
x = 100
y1 = [0] * num
cont = 0
num_threads = 2

v1 = 0
space = int(num / num_threads)
for i in range(num_threads):
    v2 = v1 + space
    m_threads.append(threading.Thread(target=thread_function, args=(y1, v1, v2)))
    m_threads[i].start()
    v1 = v2

for i in range(num_threads):
    m_threads[i].join()

end = time.time()

print("time: " + str(end - start))
##
start = time.time()

my_range = range(num)
x = 100
y = [0] * num
cont = 0
for _ in my_range:
    x = (1 / 2) + 0.0000005 + 326.15
    y[cont] = x
    cont += 1

end = time.time()

print("time: " + str(end - start))

for j in range(num):
    if y1[j] != y[j]:
        print('difer')
        print(y1[j])
        print(y[j])
        break

# https://realpython.com/intro-to-python-threading/
