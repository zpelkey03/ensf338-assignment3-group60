import heapq
import random
import time
import matplotlib.pyplot as plt

def inefficient_priority_queue_insertion(queue, element):
    queue.append(element)

def efficient_priority_queue_insertion(queue, element):
    heapq.heappush(queue, element)

def inefficient_priority_queue_extraction(queue):
    max_index = 0
    for i in range(1, len(queue)):
        if queue[i] > queue[max_index]:
            max_index = i
    return queue.pop(max_index)

def efficient_priority_queue_extraction(queue):
    return heapq.heappop(queue)

num_measurements = 100
array_size = 1000

inefficient_insertion_times = []
efficient_insertion_times = []
inefficient_extraction_times = []
efficient_extraction_times = []

for i in range(num_measurements):
    queue = []
    random_nums = [random.randint(1, 1000) for i in range(array_size)]
    start_time = time.time()
    for num in random_nums:
        inefficient_priority_queue_insertion(queue, num)
    end_time = time.time()
    inefficient_insertion_times.append(end_time - start_time)

    queue = []
    start_time = time.time()
    for num in random_nums:
        efficient_priority_queue_insertion(queue, num)
    end_time = time.time()
    efficient_insertion_times.append(end_time - start_time)

    random_nums.sort(reverse=True)
    for num in random_nums:
        inefficient_priority_queue_insertion(queue, num)

    start_time = time.time()
    while len(queue) > 0:
        inefficient_priority_queue_extraction(queue)
    end_time = time.time()
    inefficient_extraction_times.append(end_time - start_time)

    heapq.heapify(queue)
    start_time = time.time()
    while len(queue) > 0:
        efficient_priority_queue_extraction(queue)
    end_time = time.time()
    efficient_extraction_times.append(end_time - start_time)

fig, axs = plt.subplots(2, 2, figsize=(10, 10))
axs[0, 0].hist(inefficient_insertion_times)
axs[0, 0].set_title('Inefficient Insertion Times')
axs[0, 1].hist(efficient_insertion_times)
axs[0, 1].set_title('Efficient Insertion Times')
axs[1, 0].hist(inefficient_extraction_times)
axs[1, 0].set_title('Inefficient Extraction Times')
axs[1, 1].hist(efficient_extraction_times)
axs[1, 1].set_title('Efficient Extraction Times')
plt.show()


print('Inefficient Insertion Times:')
print('Min: {:.6f}'.format(min(inefficient_insertion_times)))
print('Average: {:.6f}'.format(sum(inefficient_insertion_times)/num_measurements))
print()
print('Efficient Insertion Times:')
print('Min: {:.6f}'.format(min(efficient_insertion_times)))
print('Average: {:.6f}'.format(sum(efficient_insertion_times)/num_measurements))
print()
print('Inefficient Extraction Times:')
print('Min: {:.6f}'.format(min(inefficient_extraction_times)))
print('Average: {:.6f}'.format(sum(inefficient_extraction_times)/num_measurements))
print()
print('Efficient Extraction Times:')
print('Min: {:.6f}'.format(min(efficient_extraction_times)))
print('Average: {:.6f}'.format(sum(efficient_extraction_times)/num_measurements))