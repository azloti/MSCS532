# Quick sort in Python
def quick_sort(arr):
    if len(arr) <= 1: # Base case
        return arr
    else: # Recursive case
        pivot = arr[0] # Choose the first element as the pivot
        less = [x for x in arr[1:] if x <= pivot] # Elements less than or equal to the pivot
        greater = [x for x in arr[1:] if x > pivot] # Elements greater than the pivot
        return quick_sort(less) + [pivot] + quick_sort(greater) # Recursively sort the sub-arrays


# A profiler method, you pass a function and its arguments, and it will return the time taken to execute the function and memory usage
def profiler(alg, func, *args):
    import time
    import resource
    start_time = time.time()
    start_mem = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    result = func(*args)
    end_mem = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    end_time = time.time()
    print("Algorithm: ", alg)
    print("Input: ", args[0])
    print("Result: ", result)
    print("Time taken in ms: ", (end_time - start_time) * 1000)
    print("Memory used in bytes: ", end_mem - start_mem)
    print("")


# Test cases
test_cases = [
    [3, 6, 8, 10, 1, 2, 1],
    [1, 0, 0, 1, 0, 1],
    [1, 2, 3, 4, 5],
    [5, 4, 3, 2, 1]
]

for i in range(len(test_cases)):
    profiler("Quick Sort", quick_sort, test_cases[i])
    
