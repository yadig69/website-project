# Implement a simple bubble sort in a script bubble_sort_demo.py:
def bubble_sort(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        # Flag to optimize: if no swapping occurs, array is sorted
        swapped = False
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # If no swapping occurred, array is sorted
        if not swapped:
            break
    return arr
print(bubble_sort([64, 25, 12, 22, 11]))

# Use a list of unsorted integers (you can use a fixed example list like [64, 25, 12, 22, 11] or a list of random numbers).
# Implement the bubble sort algorithm using nested loops:
# Loop through the list elements, and for each element, loop through the list again comparing adjacent pairs.
# Swap elements if they are in the wrong order.
# Continue until the list is sorted.
# Print the list at each pass of the outer loop to show the progress of the sorting.
# Finally, print the sorted list.