import time
import random
import numpy as np
import matplotlib.pyplot as plt

def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1

n = 10000
arr = np.arange(n)

start = time.time()
for i in range(100):
    x = random.randint(0, n-1)
    binary_search(arr, x)
end = time.time()
time_taken = end - start
print("Execution time of binary search:", time_taken)

plt.hist([binary_search(arr, random.randint(0, n-1)) for i in range(1000)])
plt.show()

results = []
for i in range(100):
    start = time.time()
    x = random.randint(0, n-1)
    binary_search(arr, x)
    end = time.time()
    time_taken = end - start
    results.append(time_taken)
print("Aggregate of measured values in binary search:", np.average(results))

def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

n = 10000
arr = np.arange(n)

start = time.time()
for i in range(100):
    x = random.randint(0, n-1)
    linear_search(arr, x)
end = time.time()
time_taken = end - start
print()
print("Execution time of linear search:", time_taken)

plt.hist([linear_search(arr, random.randint(0, n-1)) for i in range(1000)])
plt.show()

results = []
for i in range(100):
    start = time.time()
    x = random.randint(0, n-1)
    linear_search(arr, x)
    end = time.time()
    time_taken = end - start
    results.append(time_taken)
print("Aggregate of measured values in linear search:", np.average(results))
