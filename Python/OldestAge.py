def oldestage(age1, age2, age3):
  if age1 >= age2 and age1 >= age3:
    print(age1)
  elif age2 >= age1 and age2 >= age3:
    print(age2)
  else:
    print(age3)

#oldestage(20, 30, 40)

age1 = input("enter age 1 :")
age2 = input("enter age 2 :")
age3 = input("enter age 3 :")


oldestage(age1, age2, age3)