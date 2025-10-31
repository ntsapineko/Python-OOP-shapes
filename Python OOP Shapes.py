class Shape:
    def draw(self):
        raise NotImplementedError("draw() missing")


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def draw(self):
        if self.width <= 0 or self.height <= 0:
            print("Width and heigth must be positive integers.")
            return

        for i in range(self.height):
            print("*" * self.width)


class Triangle(Shape):
    def __init__(self, height):
        self.height = height

    def draw(self):
        if self.height <= 0:
            print("Height must be positive integer.")
            return

        for i in range(1, self.height + 1):
            stars = "*" * (2 * i - 1)
            spaces = " " * (self.height - i)
            print(spaces + stars)


class Parallelogram(Shape):
    def __init__(self, size):
        self.size = size

    def draw(self):
        if self.size <= 0:
            print("Size must be a positive integer.")
            return

        for i in range(self.size, 0, -1):
            print((" " * i) + "*" * 10)


if __name__ == "__main__":
    rect = Rectangle(10, 5)
    rect.draw()
    print()

    tri = Triangle(5)
    tri.draw()
    print()

    para = Parallelogram(5)
    para.draw()
    print()
