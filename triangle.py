import math

class Triangle:
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def calculate_perimeter(self):
        return self.side1 + self.side2 + self.side3

    def calculate_area(self):
        s = self.calculate_perimeter() / 2
        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))

if __name__ == "__main__":
    side1 = float(input("Enter the length of side 1: "))
    side2 = float(input("Enter the length of side 2: "))
    side3 = float(input("Enter the length of side 3: "))

    triangle = Triangle(side1, side2, side3)

    perimeter = triangle.calculate_perimeter()
    area = triangle.calculate_area()

    print("Perimeter of the triangle:", perimeter)
    print("Area of the triangle:", area)
