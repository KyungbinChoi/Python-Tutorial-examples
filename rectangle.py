class Rectangle:

    def __init__(self, width = 1 , height = 1):
        self.width = width
        self.height = height
    def setWidth(self, width):
        self.width = width
    def setHeight(self, height):
        self.height = height
    def getWidth(self):
        return self.width
    def getHeight(self):
        return self.height
    def area(self):
        return self.height * self.width
    def perimeter(self):
        return 2*(self.width + self.height)
    def diagonal(self):
        return (self.width**2 + self.height**2)**0.5
    def __eq__(self, other):
        if (self.width == other.width) and (self.height == other.height):
            return True
        else:
            return False

    def __str__(self):
        return "Width: "+str(self.width) +"\n"+"Height: "+str(self.height)


class Square(Rectangle):
    def __init__(self, width =1):
        self.width = width
        self.height = width

    def __str__(self):
        return "The square's Width = Height = " + str(self.width)