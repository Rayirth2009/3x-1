n = int(input("Enter a number: "))

#If the number is even
def even():
    global n
    print(n/2)
    n = n/2

#If the number is odd
def odd():
    global n
    print((3*n) + 1)
    n = 3*n + 1
    
#To solve the equation
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
