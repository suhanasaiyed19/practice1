#write a program to assert the user enters a number greater then zero.
num = int(input("Enter a number greater than zero: "))

# Assert that the number is greater than zero
assert num > 0, "Number must be greater than zero!"

print("You entered:", num)