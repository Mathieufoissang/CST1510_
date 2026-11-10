"""Rectangle Class

Create a Rectangle with width and height and area() and perimeter() methods.
Create a list of 4 rectangles, print each one's area and perimeter, then print
which rectangle has the largest area.
"""


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


rectangles = [
    Rectangle(3, 5),
    Rectangle(4, 4),
    Rectangle(6, 2),
    Rectangle(5, 7),
]

for number, rectangle in enumerate(rectangles, start=1):
    print(
        f"Rectangle {number} ({rectangle.width} x {rectangle.height}): "
        f"area = {rectangle.area()}, perimeter = {rectangle.perimeter()}"
    )

largest = max(rectangles, key=lambda rectangle: rectangle.area())
largest_number = rectangles.index(largest) + 1
print(
    f"Rectangle {largest_number} has the largest area: "
    f"{largest.area()} square units."
)
