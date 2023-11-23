## factorial
# n! = n*(n-1)*(n-1)-1)*...
# n! = n * (n-1)!

## count from 10 to 0

# loop variant
print("for-loop:")
for n in range(10, -1, -1):
    print(n)

print()

# recursion
# Python note: default recursion limit - 1000
def back_counter(n):
    print(n)

    if n <= 0:
        return

    back_counter(n-1)

print("recursion:")
back_counter(10)


def forward_counter(n, current=1):
    if current > n:
        return

    print(current)

    forward_counter(n, current+1)
