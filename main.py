n = int(input("Enter a number: "))

def even():
    global n
#    print(n)
    print(n/2)
    n = n/2

def odd():
    global n
#    print(n)
    print((3*n) + 1)
    n = 3*n + 1

def solve():
    global n
    if n%2 == 0:
        even()
    else:
        odd()
    if n!=1:
        solve()
    else:
        print("")

solve()
