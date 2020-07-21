def binary_search(arr, target, start=0, end=None):
    # Handle empty lists
    if len(arr) == 0:
        return -1

    # Default end if none is specified, for ease of use
    if end is None:
        end = len(arr)-1
    
    # Base case: only one option left
    if end - start == 0:
        if arr[start] == target:
            return start
        else:
            return -1
    
    # Check midpoint
    mid = start + (end-start) // 2
    # print("Searching for", target, "between points", start, mid, end)
    # if end < start:
    #     quit()
    if target < arr[mid]:
        # Search left half
        if mid == start:
            return binary_search(arr, target, start, mid)
        else:
            return binary_search(arr, target, start, mid-1)
    elif target > arr[mid]:
        # Search right half
        if mid == end:
            return binary_search(arr, target, mid, end)
        else:
            return binary_search(arr, target, mid+1, end)
    else:  # if target == arr[mid]
        return mid

""" logic reversed to handle lists sorted in descending order """
def binary_search_descending(arr, target, start=0, end=None):
    # Handle empty lists
    if len(arr) == 0:
        return -1

    # Default end if none is specified, for ease of use
    if end is None:
        end = len(arr)-1
    
    # Base case: only one option left
    if end - start == 0:
        if arr[start] == target:
            return start
        else:
            return -1
    
    # Check midpoint
    mid = start + (end-start) // 2
    if target > arr[mid]:
        # Search left half
        if mid == start:
            return binary_search_descending(arr, target, start, mid)
        else:
            return binary_search_descending(arr, target, start, mid-1)
    elif target < arr[mid]:
        # Search right half
        if mid == end:
            return binary_search_descending(arr, target, mid, end)
        else:
            return binary_search_descending(arr, target, mid+1, end)
    else:  # if target == arr[mid]
        return mid

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Handle empty lists
    if len(arr) == 0:
        return -1
    elif len(arr) == 1:
        if arr[0] == target:
            return 0
        else:
            return -1
    elif arr[0] < arr[-1]:
        # arr is sorted ascending
        return binary_search(arr, target)
    else: 
        # arr is sorted descending (or all one value)
        return binary_search_descending(arr, target)
