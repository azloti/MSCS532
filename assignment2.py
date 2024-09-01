import time
import resource
import random

# Quick sort
def quick_sort(arr):
    if len(arr) <= 1: # Base case
        return arr
    else: # Recursive case
        pivot = arr[0] # Choose the first element as the pivot
        less = [x for x in arr[1:] if x <= pivot] # Elements less than or equal to the pivot
        greater = [x for x in arr[1:] if x > pivot] # Elements greater than the pivot
        return quick_sort(less) + [pivot] + quick_sort(greater) # Recursively sort the sub-arrays

# Merge two sorted arrays for merge sort
def merge(left, right):
    result = [] # The merged array
    i, j = 0, 0 # Indexes for the left and right arrays
    while i < len(left) and j < len(right): # Merge the two arrays
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    # Append the remaining elements
    result += left[i:]
    result += right[j:]
    return result

# Merge sort
def merge_sort(arr):
    if len(arr) <= 1: # Base case
        return arr
    else: # Recursive case
        mid = len(arr) // 2 # Find the middle index
        left = merge_sort(arr[:mid]) # Recursively sort the left half
        right = merge_sort(arr[mid:]) # Recursively sort the right half
        # Merge the sorted halves
        return merge(left, right)

# A profiler method, you pass a function and its arguments, and it will return the time taken to execute the function and memory usage
def profiler(alg, func, *args):
    start_time = time.time()
    start_mem = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    result = func(*args)
    end_mem = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    end_time = time.time()
    # print(alg, args[0], " -> ", result)
    print(alg, "Time in ms: ", (end_time - start_time) * 1000, "Memory in bytes: ", end_mem - start_mem)


# Test cases
test_cases = [

    [random.randint(0, 10000) for i in range(10000)], # Random numbers
    [i for i in range(100)], # Sorted numbers
    [i for i in range(100, 0, -1)], # Reverse sorted numbers
]

for i in range(len(test_cases)):
    # print("Test case ", test_cases[i])
    profiler(f'Quick Sort #{i+1} - {len(test_cases[i])}', quick_sort, test_cases[i])
    profiler(f'Merge Sort #{i+1} - {len(test_cases[i])}', merge_sort, test_cases[i])
    print("")

print("Done")