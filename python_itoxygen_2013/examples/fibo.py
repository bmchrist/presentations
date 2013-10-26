# Fibonacci numbers module
# named fib.py in the current directory

def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while b < n:
        print b,
        a, b = b, a+b

def fib2(n): # return Fibonacci series up to n
    fib(n)

if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))
