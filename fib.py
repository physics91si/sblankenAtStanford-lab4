#!/usr/bin/python
# Physics 91SI
# Spring 2015
# Lab 01
# Part 1
# Solution

import sys

def main():
    args = sys.argv[1:]
    if len(args) == 0:
        args = ["error"]
    if args[0] == "help":
        help_message = \
"""

fib.py

Usage
  - './fib.py approx n': display the n-th order Fibonacci approximation to
    the golden ratio.
  - './fib.py converge': keep calculating higher-order Fibonacci approximations
    to the golden ratio until it stops changing (to floating-point precision).
  - './fib.py help': display this help message.

"""
        print help_message
    elif args[0] == "approx" and len(args) == 2:
        phi_approx(int(args[1]))
    elif args[0] == "converge" and len(args) == 1:
        phi_converge()
    else:
        print "Error: input not understood.\n" \
                "    Type './fib.py help' for info on this program."

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

phi_approx_output_format = \
"""Approximation order: {:d}
    fib_n: {:g}
    fib_(n-1): {:g}
    phi: {:.25f}"""

def phi_approx(n, show_output=True):
    """Return the nth-order Fibonacci approximation to the golden ratio."""
    fib_n = fib(n)
    fib_nm1 = fib(n - 1)
    phi = float(fib_n)/fib_nm1
    if show_output:
        print phi_approx_output_format.format(n, fib_n, fib_nm1, phi)
    return phi

phi_converge_output_format = \
"""Approximation order: {:d}
    phi_old: {:.25f}
    phi_new: {:.25f}"""

def phi_converge():
    """Keep calculating higher-order Fibonacci approximations to the golden
    ratio until it stops changing (to floating-point precision)."""

    i = 3
    phi_old = phi_approx(i - 1, show_output=False)
    phi_new = phi_approx(i)
    while phi_old != phi_new:
        i += 1
        phi_old = phi_new
        phi_new = phi_approx(i, show_output=False)
        print phi_converge_output_format.format(i, phi_new, phi_old)
    print "\nConverged to %.25f" % phi_new

if __name__ == '__main__': main()
