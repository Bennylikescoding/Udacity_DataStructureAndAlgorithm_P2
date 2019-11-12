def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    #To achieve the goal that the expected time complexity is O(log(n)), we consider using binary search.
    #The idea is like this:
    #define lower_number = 0, and a upper_number = input, create a imaginary list of [lower_number, upper_number], this list is dynamically changing;
    #1. Find the center of the list, tracking both lower and upper limit
    #2. Check to see if the target i equals the square of the center element
    #3. If it is, return that element
    #4. If less, move the upper bound to the current center
    #5. If greater, move the lower bound to the current center
    #6. Repeat 1 to 6, until lower bound = upper bound - 1, and return the element at the lower bound
    
    # 1. Tracking lower and upper bound of a imaginary list:
    lower_index = 0
    upper_index = number
    
    # Steps 2-6:
    if number == 0: # Rule out specific case
        return 0
    elif number == 1: # Rule out specific case
        return 1
    else:
        while lower_index < upper_index - 1:
            mid_index = (lower_index + upper_index) // 2
            
            if mid_index ** 2 == number:
                return mid_index
            elif mid_index ** 2 > number:
                upper_index = mid_index
            else:
                lower_index = mid_index
        return lower_index

# Test cases:

print ("Pass" if  (3 == sqrt(9)) else "Fail")
# Pass
print ("Pass" if  (0 == sqrt(0)) else "Fail")
# Pass
print ("Pass" if  (4 == sqrt(16)) else "Fail")
# Pass
print ("Pass" if  (1 == sqrt(1)) else "Fail")
# Pass
print ("Pass" if  (5 == sqrt(27)) else "Fail")
# Pass
print ("Pass" if  (7 == sqrt(50)) else "Fail")
# Pass
print("\n")
print("Large number test 1:")
print ("Pass" if  (31920 == sqrt(1018890234)) else "Fail")
# Pass
print("Large number test 2:")
print ("Pass" if  (379182 == sqrt(143778990654)) else "Fail")
# Pass

