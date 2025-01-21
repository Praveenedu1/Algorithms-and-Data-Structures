import random

def randomized_partition(arr, low, high):
    pivot_index = random.randint(low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]  # Swap pivot with last element
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def randomized_quicksort(arr, low, high):
    if low < high:
        pi = randomized_partition(arr, low, high)
        randomized_quicksort(arr, low, pi - 1)
        randomized_quicksort(arr, pi + 1, high)

# Wrapper function for ease of use
def quicksort(arr):
    if not arr:  # Handle empty array
        return arr
    randomized_quicksort(arr, 0, len(arr) - 1)
    return arr

# Example usage
arr = [10, 7, 8, 9, 1, 5]
print("Original Array:", arr)
sorted_arr = quicksort(arr)
print("Sorted Array:", sorted_arr)
