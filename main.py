from circle_area import circle_area


if __name__ == "__main__":
    radius_metres = 5
    area = circle_area(radius_metres)
    print(f"Area of a circle with radius {radius_metres} m: {area:.2f} m^2")