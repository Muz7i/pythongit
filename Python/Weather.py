temp = int(input("enter temp"))
hum= int(input("enter humidity"))


def weather(temp,hum):
  if temp >= 30 and hum >=90 :
    print("hot and humid")
  elif temp >= 30 and hum <90 :
    print("hot ")
  elif temp < 30 and hum >=90 :
    print("cool and humid")
  elif temp < 30 and hum <90 :
    print("cool ")  



weather(temp,hum)