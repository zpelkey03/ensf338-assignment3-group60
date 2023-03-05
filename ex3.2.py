import json
import urllib.request

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
        mid = (low + high) // 2 if mid == start_midpoint else mid // 2
    
    return -1

