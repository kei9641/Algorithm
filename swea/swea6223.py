class Circle:
    def __init__(self, radius):
        self.__radius = radius
    def get_area(self):
        return 3.14 * self.__radius * self.__radius

circle = Circle(2)
print('원의 면적: {}' .format(circle.get_area()))