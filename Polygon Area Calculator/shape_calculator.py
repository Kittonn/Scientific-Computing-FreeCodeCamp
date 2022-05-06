class Rectangle:
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def __str__(self) -> str:
        return 'Rectangle(width={}, height={})'.format(self.w, self.h)

    def set_width(self, w):
        self.w = w

    def set_height(self, h):
        self.h = h

    def get_area(self) -> float:
        return self.w * self.h

    def get_perimeter(self) -> float:
        return 2 * self.w + 2 * self.h

    def get_diagonal(self) -> float:
        return ((self.w ** 2 + self.h**2) ** 0.5)

    def get_picture(self) -> str:
        if (self.w > 50 or self.h > 50):
            return "Too big for picture."
        picture = (self.w * '*' + '\n') * self.h
        return picture

    def get_amount_inside(self, obj) -> float:
        return self.get_area() // obj.get_area()


class Square(Rectangle):
    def __init__(self, s):
        super().__init__(s, s)

    def __str__(self) -> str:
        return 'Square(side={})'.format(self.w)

    def set_side(self, s):
        self.w = s
        self.h = s
