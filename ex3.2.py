import json
import urllib.request
import timeit
import matplotlib.pyplot as plt

array_url = 'https://raw.githubusercontent.com/ldklab/ensf338w23/main/assignments/assignment3/ex2data.json'
searchtasks_url = 'https://raw.githubusercontent.com/ldklab/ensf338w23/main/assignments/assignment3/ex2tasks.json'

with urllib.request.urlopen(array_url) as url:
    array = json.loads(url.read().decode())

with urllib.request.urlopen(searchtasks_url) as url:
    search_tasks = json.loads(url.read().decode())

def binary_search(arr, x, start_midpoint):
    low = 0
    high = len(arr) - 1
    mid = start_midpoint
    while low <= high:
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
        mid = (low + high) // 2 if mid == start_midpoint else (low + high) // 2
    return -1

# Midpoints were calculated by using random.sample(array, 10) to find 10 random numbers from the array
random_midpoints = [78673, 352722, 128871, 579923, 656774, 239387, 210237, 482189, 291979, 191585]

fastest_times = {}
task_midpoints = {}
for task in search_tasks:
    fastest_time = float('inf')
    for midpoint in random_midpoints:
        # measure the time it takes to execute the binary search
        start_time = timeit.default_timer()
        index = binary_search(array, task, midpoint)
        end_time = timeit.default_timer()

        # calculate the execution time in milliseconds
        execution_time = (end_time - start_time) * 1000

        # update the fastest time and midpoint for this task
        if execution_time < fastest_time:
            fastest_time = execution_time
            fastest_midpoint = midpoint

    fastest_times[task] = fastest_time
    task_midpoints[task] = fastest_midpoint

# create a scatter plot of tasks and their corresponding midpoints
plt.scatter(task_midpoints.keys(), task_midpoints.values())
plt.xlabel("Task")
plt.ylabel("Midpoint")
plt.yticks(random_midpoints)
plt.ticklabel_format(style='plain')
plt.title("Midpoints for Each Task")
plt.show()