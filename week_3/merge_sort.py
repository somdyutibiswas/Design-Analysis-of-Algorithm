# Merge Sort using Divide and Conquer

def merge(arr, low, mid, high):
    left = arr[low:mid+1]
    right = arr[mid+1:high+1]

    i = j = 0
    k = low

    # Merge two sorted arrays
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    # Remaining elements
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1


def merge_sort(arr, low, high):

    # Divide
    if low < high:
        mid = (low + high) // 2

        # Conquer
        merge_sort(arr, low, mid)
        merge_sort(arr, mid + 1, high)

        # Combine
        merge(arr, low, mid, high)


# ---- User Input ----
n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter elements: ").split()))

merge_sort(arr, 0, n - 1)

print("Sorted array:")
print(arr)
