#Exercise 3.3 for assignment 3 in ENSF 338

import sys  #Used for the sys.getsizeof

empty_array_size = sys.getsizeof([]) #gets the size of an empty list to use later
max_capacity = 0 #Sets it to 0 assuming there is an empty list

for i in range(64):
    lst = list(range(i))
    new_capacity = sys.getsizeof(lst)
    if new_capacity > max_capacity:
        #prints the capacity minus the allocation size of a list in python
        # to give the allocation of bytes just in terms of data
        print(f"List capacity is now {new_capacity-empty_array_size} bytes the new capacity is {i} elements")
        max_capacity = new_capacity
