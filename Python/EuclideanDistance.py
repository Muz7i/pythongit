import math
x1 = int(input("Enter the coordinate x1: "))
x2 = int(input("Enter the coordinate x2: "))
y1 = int(input("Enter the coordinate y1: "))
y2 = int(input("Enter the coordinate y2: "))
def calculateDistance(x1,y1,x2,y2):
 dist = math.sqrt((x2-x1)**2 + (y2-y1)**2)
 return dist

print(calculateDistance(x1, y1, x2, y2))