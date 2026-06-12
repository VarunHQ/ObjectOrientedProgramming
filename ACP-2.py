class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return (22/7) * self.radius * self.radius

    def perimeter(self):
        return 2 * (22/7) * self.radius

c = Circle(float(input("Enter the radius: ")))

print("Area =", c.area())
print("Perimeter =", c.perimeter())