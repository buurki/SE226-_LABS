geometry_utils.py

import math

def circle_area(radius):
    try:
        radius = float(radius)
        if radius <= 0:
            raise ValueError("Radius must be strictly positive.")
        return math.pi * radius ** 2
    except ValueError as e:
        raise ValueError(f"Input Error: {e}")


def circle_perimeter(radius):
    radius = float(radius)
    if radius <= 0:
        raise ValueError("Input Error: Radius must be strictly positive.")
    return 2 * math.pi * radius


def rectangle_area(width, height):
    width = float(width)
    height = float(height)
    if width <= 0 or height <= 0:
        raise ValueError("Input Error: Dimensions must be strictly positive.")
    return width * height


def rectangle_perimeter(width, height):
    width = float(width)
    height = float(height)
    if width <= 0 or height <= 0:
        raise ValueError("Input Error: Dimensions must be strictly positive.")
    return 2 * (width + height)


def triangle_area(base, height):
    base = float(base)
    height = float(height)
    if base <= 0 or height <= 0:
        raise ValueError("Input Error: Dimensions must be strictly positive.")
    return 0.5 * base * height



shape_calculator.py

import geometry_utils

operations = {
    "circle_area": geometry_utils.circle_area,
    "circle_perimeter": geometry_utils.circle_perimeter,
    "rectangle_area": geometry_utils.rectangle_area,
    "rectangle_perimeter": geometry_utils.rectangle_perimeter,
    "triangle_area": geometry_utils.triangle_area,
}


def main():
    print("Available shapes: circle, rectangle, triangle")
    print("Available calculations: _area, _perimeter (e.g., circle_area)")

    operation = input("Enter the operation you want to perform: ").strip().lower()

    if operation not in operations:
        print("Input Error: Invalid operation.")
        return

    try:
        if operation.startswith("circle"):
            radius = float(input("Enter radius: "))
            result = operations[operation](radius)

        elif operation.startswith("rectangle"):
            width = float(input("Enter width: "))
            height = float(input("Enter height: "))
            result = operations[operation](width, height)

        elif operation.startswith("triangle"):
            base = float(input("Enter base: "))
            height = float(input("Enter height: "))
            result = operations[operation](base, height)

        print(f"Result: {result:.2f}")

    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()



data_package

cleaner.py



analyzer.py


__init__.py
