def cube(num):
  return num **3



num1 = int(input("Enter num1 :"))
num2 = int(input("Enter num2 :"))
num3 = int(input("Enter num3 :"))

  
armstrong = cube(num1) + cube(num2) + cube(num3)

print(armstrong)

print("This is your Armstrong number!")