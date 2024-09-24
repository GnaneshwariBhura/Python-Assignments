
# Modify above function to take third parameter shape type. It can be either "triangle" or "rectangle". Based on shape type it will calculate area. Equation of rectangle's area is,
# rectangle area=length*width
# If no shape is supplied then it should take triangle as a default shape

def calculate_area(length, width, shape_type="triangle"):
    if shape_type == "rectangle":
        return length * width
    elif shape_type == "triangle":
        return 0.5 * length * width
    else:
        raise ValueError("Invalid shape type. Choose 'triangle' or 'rectangle'.")

