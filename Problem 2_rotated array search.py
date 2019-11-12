def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    # To achieve the goal that the expected time complexity is O(log(n)), we consider using binary search.
    # The only thing that is different from a regular binary search (from the coursework) is that we here must
    #add new structures, or conditions, given that the list is rotated.
    # The problem is like this: 
    # Given a list [6, 7, 8, 9, 10, 1, 2, 3, 4], and the target is 1, find the index that matches the target.
    # Using a normal binary search, we first cut the list into [6, 7, 8, 9, 10] and [1, 2, 3, 4]
    # Then we search the left list, however, the left list is greater than the right search, which will result in error.
    # To solve this issue, we need extra structures to ensure that the next recrusion happens in the right place, e.g.,
    #for target 1, we should search the right-handed side list instead of the left one.
    # Thus, we use a simple if statement to check if the target is indeed in the left list [6, 7, 8, 9, 10], meaning it must be larger
    #than the first element of the left list, which in this case is 6. The reason why we only check the first element
    # is because the list is still ordered, which defines the new upper bound of an ordered list.
    # In order for achieving this, an "if target >= array[start_index]" is needed.
    # OK, that is the logic of this slightly updated version of a regular binary search algorithm.
    
    # We here use the recursive method adapted from the course work to do this.
    
    return rotated_array_search_recursive(input_list, number, 0, len(input_list) - 1)

def rotated_array_search_recursive(array, target, start_index, end_index):
    
    #print ("start, end: ", start_index, end_index)
    if start_index > end_index:
        return -1
    
    mid_index = (start_index + end_index) // 2
    mid_element = array[mid_index]
    
    if target == mid_element:
        return mid_index
    elif target < mid_element:
        
        # Since 1. the list is partially sorted, and 2. the list is rotated, we need to 
        #check here if the target is also less than the first element of the lower part
        #of the list.
        
        if target >= array[start_index]: # which ensures that the target is located at the smaller left part
            return rotated_array_search_recursive(array, target, start_index, mid_index - 1)
        else: # the target is located at the larger right part
            return rotated_array_search_recursive(array, target, mid_index + 1, end_index)
        
    elif target > mid_element:
        # The same logic:
        if target <= array[end_index]:
            return rotated_array_search_recursive(array, target, mid_index + 1, end_index)
        else:
            return rotated_array_search_recursive(array, target, start_index, mid_index - 1)
    
    
def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

# Test cases:
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
#Pass
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
#Pass
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
#Pass
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
#Pass
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
#Pass
