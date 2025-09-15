"""
CMPS 2200  Assignment 1.
See assignment-01.pdf for details.
"""
# no imports needed.

def foo(x):
    """Recursive Fibonacci calculator."""
    if x < 2:
        return x
    return foo(x - 2) + foo(x - 1)


def longest_run(mylist, key):
    
    longest = 0
    run = 0
    for item in mylist:
        if item == key:
            run += 1
            if run > longest:
                longest = run
        else:
            run = 0
    return longest


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
   
    return v.longest_size if isinstance(v, Result) else int(v)


def longest_run_recursive(mylist, key):
   
    n = len(mylist)
    if n == 0:
        return Result(0, 0, 0, True)
    if n == 1:
        if mylist[0] == key:
            return Result(1, 1, 1, True)
        return Result(0, 0, 0, False)

    mid = n // 2
    left_res = longest_run_recursive(mylist[:mid], key)
    right_res = longest_run_recursive(mylist[mid:], key)

    cross_run = left_res.right_size + right_res.left_size
    best_run = max(left_res.longest_size, right_res.longest_size, cross_run)

    left_edge = left_res.left_size + (right_res.left_size if left_res.is_entire_range else 0)
    right_edge = right_res.right_size + (left_res.right_size if right_res.is_entire_range else 0)

    full_span = left_res.is_entire_range and right_res.is_entire_range

    return Result(left_edge, right_edge, best_run, full_span)
