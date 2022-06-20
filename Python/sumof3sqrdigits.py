def square(num):
  return num **2

x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))
z = int(input("Enter the third number: "))

answer = square(x) + square(y) + square(z)

print("The sum of the squares is: " + str(answer))