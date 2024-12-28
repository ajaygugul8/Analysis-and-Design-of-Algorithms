import time
import random

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def measure_time(sort_function, arr):
    start_time = time.time()
    sort_function(arr)
    end_time = time.time()
    return end_time - start_time

if __name__ == "__main__":
    sizes = [100, 1000, 5000]
    for size in sizes:
        array = [random.randint(0, 10000) for _ in range(size)]
        print(f"Array Size: {size}")
        
        quick_sort_time = measure_time(lambda x: quick_sort(x.copy()), array)
        print(f"Quick Sort Time: {quick_sort_time:.5f} seconds")
        
        insertion_sort_time = measure_time(lambda x: insertion_sort(x.copy()), array)
        print(f"Insertion Sort Time: {insertion_sort_time:.5f} seconds")
        print("-" * 30)
