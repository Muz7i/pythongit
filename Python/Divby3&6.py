def num1(num2):
  
  if num2%6 == 0:
    print("True")
  elif num2%3 == 0:
      print("Num div by 3")
  else: 
      print("The number is not divisible by 3 and 6")



num2 = int(input("Enter a number: "))
num1(num2)