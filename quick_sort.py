# Separate partition function
# ✔ Recursion used
# ✔ Pivot logic correct
# ✔ Divide & Conquer structure clear


# Quick Sort using Divide and Conquer

def partition(arr, low, high):
    pivot = arr[high]      # choose pivot
    i = low - 1

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    # place pivot at correct position
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1


def quick_sort(arr, low, high):

    # Divide & Conquer
    if low < high:

        # Divide (partition)
        pi = partition(arr, low, high)

        # Conquer (recursive calls)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)


# ---- User Input ----
n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter elements: ").split()))

quick_sort(arr, 0, n - 1)

print("Sorted array:")
print(arr)