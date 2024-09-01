# Quick sort in Python
def quick_sort(arr):
    if len(arr) <= 1: # Base case
        return arr
    else: # Recursive case
        pivot = arr[0] # Choose the first element as the pivot
        less = [x for x in arr[1:] if x <= pivot] # Elements less than or equal to the pivot
        greater = [x for x in arr[1:] if x > pivot] # Elements greater than the pivot
        return quick_sort(less) + [pivot] + quick_sort(greater) # Recursively sort the sub-arrays

# Test cases
print(quick_sort([3, 6, 8, 10, 1, 2, 1])) # [1, 1, 2, 3, 6, 8, 10]
print(quick_sort([1, 0, 0, 1, 0, 1])) # [0, 0, 0, 1, 1, 1]
print(quick_sort([1, 2, 3, 4, 5])) # [1, 2, 3, 4, 5]
print(quick_sort([5, 4, 3, 2, 1])) # [1, 2, 3, 4, 5]
