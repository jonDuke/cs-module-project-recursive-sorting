def merge(arrA, arrB):
    merged_arr = [0] * (len(arrA) + len(arrB))

    # While both sides have values left, add the smaller one
    left = 0
    right = 0
    while left < len(arrA) and right < len(arrB):
        if arrA[left] <= arrB[right]:
            # add element from arrA
            merged_arr[left+right] = arrA[left]
            left += 1
        else:
            # add element from arrA
            merged_arr[left+right] = arrB[right]
            right += 1
    
    # Add any remaining values
    while left < len(arrA):
        merged_arr[left+right] = arrA[left]
        left += 1
    
    while right < len(arrB):
        merged_arr[left+right] = arrB[right]
        right += 1

    return merged_arr


def merge_sort(arr):
    # Base case: array of length 1 or 0
    if len(arr) <= 1:
        return arr  # considered sorted, just return it
    
    # Split arr into 2 parts, sort them, then merge back together
    mid = len(arr) // 2
    return merge(merge_sort(arr[0:mid]), merge_sort(arr[mid:len(arr)]))


# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    while start <= mid-1 and mid <= end:
        # Compare start and mid
        if arr[mid] < arr[start]:
            temp = arr[mid]  # set aside mid
            for i in range(mid, start-1, -1):
                arr[i] = arr[i-1]  # shift everything to the mid
            arr[start] = temp  # insert temp into place

            # Update pointers
            mid += 1
        start += 1

def merge_sort_in_place(arr, l, r):
    # So long as r is greater than l...
    if r > l:
        # Sort the left and right halves
        mid = l + (r-l) // 2
        merge_sort_in_place(arr, l, mid)
        merge_sort_in_place(arr, mid+1, r)

        # Merge them together
        merge_in_place(arr, l, mid+1, r)
