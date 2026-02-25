# 1. Assume first element as min and max.
# 2 Compare each element:
#    if smaller → update min
#    if bigger → update max
# time complexity = O(n)

# WAP to find Min and Max using Divide and Conquer

def min_max(arr, low, high):

    # Base case: only one element
    if low == high:
        return arr[low], arr[low]

    # Base case: two elements
    if high == low + 1:
        if arr[low] < arr[high]:
            return arr[low], arr[high]
        else:
            return arr[high], arr[low]

    # Divide
    mid = (low + high) // 2

    # Conquer
    min1, max1 = min_max(arr, low, mid)
    min2, max2 = min_max(arr, mid + 1, high)

    # Combine
    minimum = min(min1, min2)
    maximum = max(max1, max2)

    return minimum, maximum


# ---- User Input ----
n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter elements: ").split()))

minimum, maximum = min_max(arr, 0, n - 1)

print("Minimum element =", minimum)
print("Maximum element =", maximum)
