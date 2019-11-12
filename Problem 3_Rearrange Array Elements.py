def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    # By examing the examples, e.g., [1, 2, 3, 4, 5] to [531, 42], and [2, 4, 5, 6, 8, 9] to [964, 852],
    #we come up with the following ideas:
    # 1. Sort the list in ascending order, using MergeSort (time complexity is O(n * log(n)))
    # Since now the new list is sorted, the problem actually converted into this:
    #the index of left list is just the even index of the original list, but instead in a descending order.
    #for example, [5,3,1] is 5(index = 4), 3(index = 2), 1(index = 0)
    # So is the case with the right list (the odd index). for example, [4,2] is 4(index = 3), 2(index = 1)
    # Thus, based on this observation, we do the following:
    # 2. Create two lists, i.e., left and right, to hold the values.
    # 2.1 Iterate through the list in a descending order, put each number into the left and right lists, respectively and successively. (time complexity is O(n))
    # 2.2 Return the lists and convert them into concatenated strings, and then wrap them in a list

    # First we started to sort the list
    sorted_list = mergesort(input_list)
    
    # Then we get our two numbers
    return get_two_number(sorted_list)

#-----------------------------------------the following are adapted from course work------
def mergesort(input_list):
    if len(input_list) <= 1:
        return input_list

    mid = len(input_list) // 2
    left = input_list[:mid]
    right = input_list[mid:]

    left = mergesort(left)
    right = mergesort(right)

    return merge(left, right)

def merge(left, right):

    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] > right[right_index]:
            merged.append(right[right_index])
            right_index += 1
        else:
            merged.append(left[left_index])
            left_index += 1

    merged += (left[left_index:]) 
    merged += (right[right_index:])

    return merged

#-----------------------------------------the above are adapted from course work------

# Now we define a function to return the two required numbers:
def get_two_number(sorted_list):

    last_index = len(sorted_list) - 1 # Get last index
    left_number = ''
    right_number = ''
    while last_index >= 0: # Time complexity is O(n)
        left_number += str(sorted_list[last_index])
        if last_index > 0: # Avoid situation that the last_index = 0, and the right_number will return sorted_list[-1]
            right_number += str(sorted_list[last_index - 1])
        last_index -= 2 # move to the next second number, which ensures we get an index array of even or odd numbers (5,3,1..., or 6,4,2,0).

    left_number = int(left_number)
    right_number = int(right_number)

    return [left_number, right_number]
# The overall time complexity is O(nlog(n)) + O(n) = O(nlog(n))

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

# Test cases:
test_function([[4, 6, 2, 5, 9, 8], [964, 852]]) 
# Pass
test_function([[1, 2, 3, 4, 5], [542, 31]])
# Pass
test_function([[6, 8, 9, 1, 2], [961, 82]])
# Pass
test_function([[0,0,0,0,0], [0, 0]])
# Pass

# Another testing case
import random
l = [i for i in range(0, 9)]  # a list containing 0 - 9
random.shuffle(l)
rearrange_digits(l)
#"[86420, 7531]"
