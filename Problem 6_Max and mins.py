def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    # To start with, we create two variables, min and max, that is equal to the length of the ints list,
    #and to dynamically track the numbers when traversing
    # During iteration, if a number is greater than the original max, then update max with that value
    # If a number is smaller than the original min, then update min with that value
    # In this case, the complexity would be O(n), in a single traverse.
    if len(ints) != 0:
        min = ints[0]
        max = ints[0] # modified according to the first reviewer's suggestion
        for i in ints:
            if i >= max:
                max = i
                #print ("max:", max)
            elif i <= min:
                min = i
                #print ("min:", min)
        return (min, max)
    else:
        return "List is empty!"

# Test cases
## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")
# Pass

l = [4,5,1,0,2]
print ("Pass" if ((0, 5) == get_min_max(l)) else "Fail")
# Pass

l = [4,1,13,15,11,19,20,12]
print ("Pass" if ((1, 20) == get_min_max(l)) else "Fail")
# Pass

l = [40,50,99,89,25,20]
print("Pass" if ((20, 99) == get_min_max(l)) else "Fail")
# Pass

l = []
print("Pass" if ("List is empty!") == get_min_max(l) else "Fail")
# Pass