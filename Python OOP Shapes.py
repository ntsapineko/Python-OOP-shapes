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


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def draw(self):
        if self.radius <= 0:
            print("Radius must be a positive integer.")
            return

        diameter = 2 * self.radius

        for y in range(diameter + 1):
            for x in range(diameter + 1):
                distancex = x - self.radius
                distancey = y - self.radius
                distance = (distancex**2 + distancey**2) ** 0.5

                if distance <= self.radius:
                    print("*", end=" ")
                else:
                    print(" ", end="")
            print()


class Rhombus(Shape):
    def __init__(self, size):
        self.size = size

    def draw(self):
        if self.size <= 0:
            print("Size must be a positive integer.")
            return

        for i in range(self.size):
            spaces_in = " " * (self.size - i - 1)
            stars = "*" + " " * (2 * i - 1)
            if i == 0:
                print(spaces_in + "*")
            else:
                print(spaces_in + stars + "*")


if __name__ == "__main__":
    rect = Rectangle(10, 5)
    rect.draw()
    print()

    tri = Triangle(8)
    tri.draw()
    print()

    rhom = Rhombus(5)
    rhom.draw()
    print()

    # circ = Circle(10)
    # circ.draw()
    # print()
