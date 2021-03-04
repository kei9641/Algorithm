class Rectangle:
    def __init__(self, width, high):
        self.__width = width
        self.__high = high
    def get_area(self):
        return self.__width * self.__high
    
rectangle = Rectangle(4, 5)
print('사각형의 면적: {}' .format(rectangle.get_area()))