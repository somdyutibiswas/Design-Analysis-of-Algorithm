# 3. Perform insertion sort, selection sort and bubble sort on the following unsorted array:  {28, 12, 15, 13, 25}

# n = int(input("Enter number of elements: "))
# arr = list(map(int, input("Enter the elements separated by space: ").split()))

# # Bubble Sort logic
# for i in range(n):
#     for j in range(0, n - i - 1):
#         if arr[j] > arr[j + 1]:
#             arr[j], arr[j + 1] = arr[j + 1], arr[j]

# # Print sorted array
# print("Sorted array using Bubble Sort:")
# print(arr)


#using function
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# User input
n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter the elements separated by space: ").split()))

# Function call
sorted_arr = bubble_sort(arr)

# Output
print("Sorted array using Bubble Sort:")
print(sorted_arr)
