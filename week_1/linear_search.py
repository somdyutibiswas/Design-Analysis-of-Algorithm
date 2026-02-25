def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i   # element found, return index
    return -1           # element not found


# User input
n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter the elements separated by space: ").split()))
key = int(input("Enter element to search: "))

# Function call
result = linear_search(arr, key)

# Output
if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found")
