# Function that shows me the log of the number
# that I enter.
def main():
    print("This program will show you the log of a number.")
    print("Please enter a number: ")
    number = int(input())
    log = math.log(number)
    print("The log of the number is: ", log)