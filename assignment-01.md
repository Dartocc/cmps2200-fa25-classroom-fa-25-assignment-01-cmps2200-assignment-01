

# CMPS 2200 Assignment 1

**Name:**_________________________


In this assignment, you will learn more about asymptotic notation, parallelism, functional languages, and algorithmic cost models. As in the recitation, some of your answer will go here and some will go in `main.py`. You are welcome to edit this `assignment-01.md` file directly, or print and fill in by hand. If you do the latter, please scan to a file `assignment-01.pdf` and push to your github repository. 
  
  

1. (2 pts ea) **Asymptotic notation** (12 pts)

  - 1a. Is $2^{n+1} \in O(2^n)$? Why or why not? 
Yes, because Adding 1 to 2^n does not change its growth. Both increase at the same exponential rate.

  - 1b. Is $2^{2^n} \in O(2^n)$? Why or why not?     
No, 2^n is not asymptotically dominant over 2^(2^n) because the limit method yields the result of infinity, which means 2^n is being asymptotically dominated. 
  
  - 1c. Is $n^{1.01} \in O(\mathrm{log}^2 n)$?    
No. A polynomial like n^1.01 always grows faster than a logarithm, so it cannot be bounded above.

  - 1d. Is $n^{1.01} \in \Omega(\mathrm{log}^2 n)$?  
Yes, log^2(n) is asymptotically dominated by n^1.01 as the limit method results in 0.
  
  - 1e. Is $\sqrt{n} \in O((\mathrm{log} n)^3)$?  
No, as the use of the limit method achieves a value of 0 which means log(n)^3 is being asymptotically dominated.

  - 1f. Is $\sqrt{n} \in \Omega((\mathrm{log} n)^3)$?  
 Yes, n is larger than (logn)^3 for big n, so it is a proper lower bound.


2. **SPARC to Python** (12 pts)

Consider the following SPARC code of the Fibonacci sequence, which is the series of numbers where each number is the sum of the two preceding numbers. For example, 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610 ... 
$$
\begin{array}{l}
\mathit{foo}~x =   \\
~~~~\texttt{if}{}~~x \le 1~~\texttt{then}{}\\
~~~~~~~~x\\   
~~~~\texttt{else}\\
~~~~~~~~\texttt{let}{}~~(ra, rb) = (\mathit{foo}~(x-1))~~,~~(\mathit{foo}~(x-2))~~\texttt{in}{}\\  
~~~~~~~~~~~~ra + rb\\  
~~~~~~~~\texttt{end}{}.\\
\end{array}
$$ 

  - 2a. (6 pts) Translate this to Python code -- fill in the `def foo` method in `main.py`  

  - 2b. (6 pts) What does this function do, in your own words?  

This function works by calling itself whenever the input value of x is greater than 1. Each call splits into two smaller calls: one with 
x−1 and one with x−2. The results of those two calls are then added together. By repeating this process, the function produces the Fibonacci number that corresponds to the position x. For example, if the function is called with x=7, it will return 13 because the values for 5 (which is 5) and 6 (which is 8) add together to make 13. 

3. **Parallelism and recursion** (26 pts)

Consider the following function:  

```python
def longest_run(myarray, key)
   """
    Input:
      `myarray`: a list of ints
      `key`: an int
    Return:
      the longest continuous sequence of `key` in `myarray`
   """
```
E.g., `longest_run([2,12,12,8,12,12,12,0,12,1], 12) == 3`  
 
  - 3a. (7 pts) First, implement an iterative, sequential version of `longest_run` in `main.py`.  

  - 3b. (4 pts) What is the Work and Span of this implementation?  
Work (total operations):
The loop visits each element of the list exactly once, performing a constant amount of work each time. So the work is O(n), where n is the length of the list.
Span (longest dependency chain): The loop is sequential: each step depends on knowing the current streak from the previous step. Therefore, the span is O(n) as well.

  - 3c. (7 pts) Next, implement a `longest_run_recursive`, a recursive, divide and conquer implementation. This is analogous to our implementation of `sum_list_recursive`. To do so, you will need to think about how to combine partial solutions from each recursive call. Make use of the provided class `Result`.   

  - 3d. (4 pts) What is the Work and Span of this sequential algorithm?  
Work (total operations):
The recursion touches every element exactly once, just like the iterative version. The combination step at each level of recursion does constant work. Therefore, the total work is still O(n).
Span (longest chain of dependencies):
Because the recursive calls are done sequentially, the recursion has depth proportional to logn, but you still have to process all subcalls one after another. This makes the span O(n).


  - 3e. (4 pts) Assume that we parallelize in a similar way we did with `sum_list_recursive`. That is, each recursive call spawns a new thread. What is the Work and Span of this algorithm?  
Work: Nothing changes, all the same computations are performed. The total work remains O(n).
Span: Now, the two recursive halves can be solved at the same time. The recursion tree has depth about logn. At each level, the combine step is constant. Therefore, the span is reduced to O(log n). 

