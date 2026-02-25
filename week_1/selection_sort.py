def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # swap
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

# User input
n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter the elements separated by space: ").split()))

# Function call
sorted_arr = selection_sort(arr)

# Output
print("Sorted array using Selection Sort:")
print(sorted_arr)
