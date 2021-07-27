# Coding challenge that teaches me how to write recursive functions
#   and how to use the 'return' statement.

def factorial(n):
    if n == 1:
        return 1
    if n <= 0:
        return "Not possible" 
    else:
        return n * factorial(n - 1)

#Evaluate the function
print(factorial(10))