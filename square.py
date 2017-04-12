import rectangle

a = rectangle.Square(3)
b = rectangle.Square(5)
print(a)
print(b)

print("The square has following measurements."+"\n"+
      "Width is " + str(a.getWidth())+"\n"+
      "Height is "+ str(a.getHeight())+"\n"+
      "The Area of the square is " + str(a.area())+"\n"+
      "The Perimeter of the square is " + str(a.perimeter()))

if a==b:
    print("The first and the second squares are same")
else:
    print("The first and the second squares are different")
