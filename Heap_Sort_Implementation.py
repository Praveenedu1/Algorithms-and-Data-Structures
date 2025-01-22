class HeapSort:
    @staticmethod
    def heapify(arr, n, i):
        largest = i  # Initialize largest as root
        left = 2 * i + 1
        right = 2 * i + 2

        # Check if left child exists and is greater than root
        if left < n and arr[left] > arr[largest]:
            largest = left

        # Check if right child exists and is greater than the largest so far
        if right < n and arr[right] > arr[largest]:
            largest = right

        # If the largest is not the root, swap and continue heapifying
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            HeapSort.heapify(arr, n, largest)

    @staticmethod
    def heapsort(arr):
        n = len(arr)

        # Build a max heap
        for i in range(n // 2 - 1, -1, -1):
            HeapSort.heapify(arr, n, i)

        # Extract elements one by one from the heap
        for i in range(n - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]  # Swap the root with the last element
            HeapSort.heapify(arr, i, 0)

        return arr

# Example Usage
if __name__ == "__main__":
    arr = [4, 10, 3, 5, 1]
    print("Original array:", arr)
    sorted_array = HeapSort.heapsort(arr)
    print("Sorted array:", sorted_array)