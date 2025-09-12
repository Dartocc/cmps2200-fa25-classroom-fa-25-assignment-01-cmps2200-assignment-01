"""
CMPS 2200  Assignment 1.
See assignment-01.pdf for details.
"""
# no imports needed.

def foo(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        x = min(a, b)
        y = max (a, b)
        return foo (y, y % x)

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
        self.left_size = left_size              # the length of the longest run on left side of input
                                                # eg, with a key of 12, [12 12 3] has left_size of 2 
        self.right_size = right_size            # length of longest run on right side of input
                                                # eg, key 12, [3 12 12] has right_size of 2
        self.longest_size = longest_size        # length of longest run in input
                                                # eg, [12 12 4 12 12 12]: longest_size is 3
        self.is_entire_range = is_entire_range  # True if the entire input matches the key
        
    def __repr__(self):
        return('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
              (self.longest_size, self.left_size, self.right_size, self.is_entire_range))
    
    
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

## Feel free to add your own tests here.
def test_longest_run():
    assert longest_run([2,12,12,8,12,12,12,0,12,1], 12) == 3

print(longest_run([2,12,12,8,12,12,12,0,12,1], 12))
print(longest_run_recursive([2,12,12,8,12,12,12,0,12,1], 12))
