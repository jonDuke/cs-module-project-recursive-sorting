def binary_search(arr, target, start=0, end=None, direction="ascending"):
    # Default end if none is specified, for ease of use
    if end is None:
        end = len(arr)-1
    
    if end >= start:
        mid = start + (end-start) // 2

        if target < arr[mid]:
            if direction == "ascending":
                # target must be in left half
                return binary_search(arr, target, start, mid-1)
            elif direction == "descending":
                # target must be in right half
                return binary_search(arr, target, mid+1, end, "descending")
        elif target > arr[mid]:
            if direction == "ascending":
                # target must be in right half
                return binary_search(arr, target, mid+1, end)
            elif direction == "descending":
                # target must be in left half
                return binary_search(arr, target, start, mid-1, "descending")
        else:
            # target found (arr[mid] == target)
            return mid
    
    # Start and end have converged without finding the target
    else:
        return -1

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
    
    # Compare first and last items to decide direction
    elif arr[0] < arr[-1]:
        return binary_search(arr, target, direction="ascending")
    else:
        return binary_search(arr, target, direction="descending")
