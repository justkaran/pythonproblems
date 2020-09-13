'''Write a function which prints every number from 0 up to the given input. If divisible by 3, print "Fizz" instead of the number. If divisible by 5, print "Buzz". If input is divisible by 3 AND 5, print "FizzBuzz".'''

#Clarify the Problem

#Create Inputs


#Outline the Solution
# a function that takes in the input as an integer. By using the modulo function the function runs through a conditional statement that tests the inputs divisibility with 3 and 5.

#Code the Solution
def fizzbuzz(input):
  if input/3 % 3 == 0:
    print ("Fizz")
  if input/5 % 5 == 0:
    print ("Buzz")
  if input/3 % 3 == 0 and input/5 % 5 == 0:
    print("FizzBuzz")

#Test the Solution
fizzbuzz(8)

#Analyze the Solution