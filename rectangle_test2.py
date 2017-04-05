import rectangle

d = rectangle.Rectangle()
d.setWidth(4)
d.setHeight(5)

print("The rectangle has following measurements."+"\n"+
      "Width is " + str(d.getWidth())+"\n"+
      "Height is "+ str(d.getHeight())+"\n"+
      "Area is " + str(d.area())+"\n"+
      "Perimeter is " + str(d.perimeter()))