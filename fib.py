def fib(a):
    print("fib("+ str (a)+") was called")
    if a < 1:
        return 1
    else:
        return fib(a-1) + fib(a-2)


print(fib(7))
