import array as arr
import matplotlib.pyplot as plt
import time

def merge_sort(input):
    n = len(input)
    if n == 1:
        return input
    halve = int(len(input)/2)
    # divide the arrays into two parts
    left = input[:halve]
    right = input[halve:]
    # sort each part 
    C = merge_sort(left)
    D = merge_sort(right)
    # merge sorted arrays into one
    def merge():
        i=0
        j=0
        nn = int(len(C) + len(D))
        half_len = int(nn/2) #if n%2 == 0 else int(nn+1/2)
        sorted = arr.array('i', [])
        for k in range(n):
            # todo fix this part
            if j == 1 and len(D) == 2:
                sorted = merge_sort(D) + C
                break
            if i == 1 and len(C) == 2:
                sorted = merge_sort(C) + D
                break
            if j == half_len:
                sorted = sorted + C
                break
            if i == half_len:
                sorted = sorted + D
                break
            elif C[i] > D[j]:
                # print("C[i]: {}, D[j]: {}".format(C[i], D[j]))
                sorted.append(D[j])
                j += 1
            else:
                sorted.append(C[i])
                i += 1
        return sorted

    return merge()

n = 1
t = []
size = []
times = 50
step = 1000
while n < times:
    input = arr.array('i', [])
    for i in range(n*step):
        input.append(n*step - i)
    start = time.time()
    result = merge_sort(input)
    # print(result)
    end = time.time()
    t.append(end - start)
    size.append(n*step)
    n += 1

plt.xlabel('n')
plt.ylabel('t = f(n)')
plt.plot(size, t)
plt.show()
