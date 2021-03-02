class Point:
    # Class attributes are shared between objects & classes
    default_color = "red"

    # A constructor is a special method

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f" Point ({self.x}, {self.y})")


Point.default_color = "Yellow"

point = Point(1, 2)
print(point.default_color)
print(Point.default_color)
# Objects in Python are dynamic
point.z = 10
point.draw()
