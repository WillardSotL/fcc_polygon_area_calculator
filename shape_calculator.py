class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, value):
        self.width = value

    def set_height(self, value):
        self.height = value

    def get_area(self):
        area = self.width * self.height
        return area

    def get_perimeter(self):
        perimeter = 2 * self.width + 2 * self.height
        return perimeter

    def get_diagonal(self):
        diagonal = (self.width ** 2 + self.height ** 2) ** .5
        return diagonal

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        picture = ""
        for i in list(range(self.height)):
            picture += "*" * self.width + "\n"
        return picture

    def get_amount_inside(self, shape):
        fitshape_width = self.width // shape.width
        fitshape_height = self.height // shape.height
        return fitshape_width * fitshape_height

    def __str__(self):
        string_rectangle = f'Rectangle(width={self.width}, height={self.height})'
        return string_rectangle

class Square(Rectangle):
    def __init__(self, side):
        self.side = side
        self.width = self.height = self.side

    def set_side(self, value):
        self.set_width(value)
        self.set_height(value)

    def __str__(self):
        string_square = f'Square(side={self.width})'
        return string_square
