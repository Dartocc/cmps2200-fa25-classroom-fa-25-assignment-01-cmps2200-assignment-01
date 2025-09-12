"""
CMPS 2200  Assignment 1.
See assignment-01.pdf for details.
"""
# no imports needed.

def foo(x):
    if x <= 1:              # base case
        return x
    else:                   # recursive case
        ra = foo(x - 1)
        rb = foo(x - 2)
        return ra + rb


def longest_run(mylist, key):
    counter = 0
    maxcount = 0
    for i in mylist:
        if i == key:
            counter += 1
            maxcount = max(maxcount, counter)
        else:
            counter = 0
    return maxcount

class Result:
    """ done """
    def __init__(self, left_size, right_size, longest_size, is_entire_range):
        self.left_size = left_size               # run on left side of input
        self.right_size = right_size             # run on right side of input
        self.longest_size = longest_size         # longest run in input
        self.is_entire_range = is_entire_range   # True if the entire input matches the key
        
    def __repr__(self):
        return('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
              (self.longest_size, self.left_size, self.right_size, self.is_entire_range))
    

def to_value(v):
    """
    if it is a Result object, return longest_size.
    else return v
    """
    if type(v) == Result:
        return v.longest_size
    else:
        return int(v)
        
def longest_run_recursive(mylist, key):
    # Base cases: If the list is empty or if it only has one item in it, check if the item is what we need
    if len(mylist) == 0:
        return Result(0, 0, 0, False)
    elif len(mylist) == 1:
        if mylist[0] == key:
            return Result(1, 1, 1, True)
        else:
            return Result(0, 0, 0, False)
    
    mid = len(mylist) // 2
    left_result = longest_run_recursive(mylist[:mid], key)
    right_result = longest_run_recursive(mylist[mid:], key)
    
    # Determine if entire range matches key
    is_entire = left_result.is_entire_range and right_result.is_entire_range
    
    # Left size
    left_size = left_result.left_size
    if left_result.is_entire_range:
        left_size += right_result.left_size
    
    # Right size
    right_size = right_result.right_size
    if right_result.is_entire_range:
        right_size += left_result.right_size
    
    # Longest size across middle
    longest_size = max(left_result.longest_size, 
                       right_result.longest_size,
                       left_result.right_size + right_result.left_size)
    
    return Result(left_size, right_size, longest_size, is_entire)




