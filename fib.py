# Physics 91SI
# Spring 2015
# Lab 01
# Part 1
# Solution

def fib(n):
    """Return nth element of the Fibonacci sequence."""
    # Create the base case
    n0 = 0
    n1 = 1
    
    # Loop n times. Just ignore the variable i.
    for i in range(n):
        n_new = n0 + n1
        n0 = n1
        n1 = n_new
    return n0

def phi_approx(n):
    """Return the nth-order Fibonacci approximation to the golden ratio."""
    fib_n = fib(n)
    fib_nm1 = fib(n - 1)
    phi = float(fib_n)/fib_nm1
    print n, fib_n, fib_nm1, phi
    return phi

# Find successively better approximations
for i in range(2, 15):
    print phi_approx(i)