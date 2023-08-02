import array as arr
import matplotlib.pyplot as plt
import time


def merge(left, right):
    i=0
    j=0
    # size of right and left
    n = int(len(left) + len(right))
    sorted = arr.array('i', [])
    for k in range(n):
        if j == len(right):
            sorted = sorted + left
            break
        if i == len(left):
            sorted = sorted + right
            break
        if left[i] > right[j]:
            sorted.append(right[j])
            j += 1
        else:
            sorted.append(left[i])
            i += 1
    return sorted

def merge_sort(input):
    n = len(input)
    if n == 1:
        return input
    halve = int(len(input)/2)
    # divide the arrays into two parts
    left = input[:halve]
    right = input[halve:]
    # sort each part 
    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)
    # merge sorted arrays into one
    return merge(left_sorted, right_sorted)

n = 1
t = []
size = []
times = 100
step = 1000
while n < times:
    input = arr.array('i', [])
    for i in range(n*step):
        input.append(n*step - i)
    start = time.time()
    result = merge_sort(input)
    end = time.time()
    t.append(end - start)
    size.append(n*step)
    n += 1

plt.xlabel('n')
plt.ylabel('t = f(n)')
plt.plot(size, t)
plt.ylim([0, 1])
plt.xlim([0, 120000])
plt.show()


# O(log2n)