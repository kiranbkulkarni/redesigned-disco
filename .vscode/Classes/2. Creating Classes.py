# Use Pascal naming convention
# Like Point, MyPoint
class Point:
    def draw(self):
        print("draw")


point = Point()
point.draw()
print(type(point))

print(isinstance(point, Point))
