class Point:
    # Class attributes are shared between objects & classes
    default_color = "red"

    # A constructor is a special method
    @classmethod
    def zero(cls):
        return cls(0, 0)

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f" Point ({self.x}, {self.y})")


#Point.default_color = "Yellow"

point = Point(1, 2)
zero_point = Point.zero()

print(point)
print(zero_point)
