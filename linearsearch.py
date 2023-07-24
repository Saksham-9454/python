def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i # Return the index if the element is found
            return -1 # Return -1 if the element is not found
# Example usage
my_list = [10, 3, 7, 5, 2, 9]
target_element = 5
result = linear_search(my_list, target_element)
if result != -1:
    print("Element", target_element, "found at index", result)
else:
    print("Element", target_element, "not found in the list")