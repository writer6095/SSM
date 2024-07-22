def draw_circle(radius):
    x = 0
    y = radius
    d = 1 - radius  # Initial decision parameter

    points = []  # List to store the boundary points

    while y > x:
        points.append((x, y))  # Points in the first octant

        if d < 0:
            d += 2 * x + 3  # Move to E (East)
        else:
            d += 2 * (x - y) + 5  # Move to SE (Southeast)
            y -= 1

        x += 1

    return points

# Define the radius
radius = 8

# Get the coordinates of the circular boundary in the first quadrant
boundary_points = draw_circle(radius)

# Display the coordinates
for point in boundary_points:
    print(f"({point[0]}, {point[1]})")
