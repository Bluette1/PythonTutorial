# Instructions from your teacher:
# Statement
#
# Write a program that reads an integer number and prints its previous and next numbers. See the example below.
#
#
# Example input
#
# 179
#
#
# Example output
#
# The next number for the number 179 is 180
# The previous number for the number 179 is 178
#
#
# Theory
#
# If you don't know how to start solving this assignment, please, review a theory for this lesson:
# https://snakify.org/lessons/print_input_numbers/
#
# You may also try step-by-step theory chunks:
# https://snakify.org/lessons/print_input_numbers/steps/1/

numberStr = input()
number = int(numberStr)
nextInt = number + 1
nextStr = str(nextInt)
previousInt = number - 1
previousStr = str(previousInt)

print("The next number for the number " + numberStr + " is " + nextStr)

print("The previous number for the number " + numberStr + " is " + previousStr)
