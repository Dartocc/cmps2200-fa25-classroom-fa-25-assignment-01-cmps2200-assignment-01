"""
CMPS 2200  Assignment 1.
See assignment-01.pdf for details.
"""
# no imports needed.

def foo(x):
    if x <= 1:
      return x
    else:
      return (foo(x - 1) + foo(x - 2))

def longest_run(mylist, key):
  run = 0
  max_run = 0
  for x in mylist:
    if x == key:
      run += 1
    else:
      if run > max_run:
        max_run = run
        run = 0
      else:
        run = 0
  return max_run

class Result:
    def __init__(self, left_size, right_size, longest_size, is_entire_range):
        self.left_size = left_size               # run on left side of input
        self.right_size = right_size             # run on right side of input
        self.longest_size = longest_size         # longest run in input
        self.is_entire_range = is_entire_range   # True if the entire input matches the key
        
    def __repr__(self):
        return('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
              (self.longest_size, self.left_size, self.right_size, self.is_entire_range))
  
def longest_run_recursive(mylist, key):
  if len(mylist) == 1:
    if mylist[0] == key:
      return Result(1, 1, 1, True)
    else:
      return Result(0, 0, 0, False)
  elif len(mylist) == 0:
    return Result(0, 0, 0, False)
  else:
    mid = len(mylist) // 2
    l = mylist[:mid]
    r = mylist[mid:]
    a0 = Result(0, 0, 0, False)
    l0 = longest_run_recursive(l, key)
    r0 = longest_run_recursive(r, key)

    if l0.is_entire_range == True and r0.is_entire_range == True:
      a0.left_size = l0.longest_size + r0.longest_size
      a0.longest_size = l0.longest_size + r0.longest_size
      a0.right_size = l0.longest_size + r0.longest_size
      a0.is_entire_range = True
      return a0
    else:
      if l0.is_entire_range == True:
        a0.left_size = l0.longest_size + r0.left_size
        a0.longest_size = max(l0.longest_size, r0.longest_size, l0.right_size + r0.left_size)
        a0.right_size = r0.right_size
      elif r0.is_entire_range == True:
        a0.right_size = r0.longest_size + l0.right_size
        a0.left_size = l0.left_size
        a0.longest_size = max(l0.longest_size, r0.longest_size, l0.right_size + r0.left_size)
      else:
        a0.left_size = l0.left_size
        a0.longest_size = max(l0.longest_size, r0.longest_size, l0.right_size + r0.left_size)
        a0.right_size = r0.right_size
      return a0

def test_longest_run():
    assert longest_run([2,12,12,8,12,12,12,0,12,1], 12) == 3

def test_longest_run_recursive():
    assert longest_run_recursive([2,12,12,8,12,12,12,0,12,1], 12).longest_size == 3
