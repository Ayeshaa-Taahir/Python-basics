import sys
import math

# Ensure the user provides exactly one argument (the angle)
if len(sys.argv) != 2:
    print("Usage: python angle_functions.py <angle_in_degrees>")
    sys.exit(1)

try:
    # Convert the input to a float (angle in degrees)
    angle_degrees = float(sys.argv[1])

    # Convert degrees to radians
    angle_radians = math.radians(angle_degrees)

    # Calculate trigonometric values
    sin_val = math.sin(angle_radians)
    cos_val = math.cos(angle_radians)

    # Check for undefined tangent (when cosine ≈ 0)
    if abs(cos_val) < 1e-10:
        tan_val = "undefined (cosine is zero)"
    else:
        tan_val = math.tan(angle_radians)

    # Print the results
    print(f"\nTrigonometric Functions for {angle_degrees}°:\n")
    print(f"   sin({angle_degrees}) = {sin_val}")
    print(f"   cos({angle_degrees}) = {cos_val}")
    print(f"   tan({angle_degrees}) = {tan_val}")

except ValueError:
    print("\nPlease enter a valid numeric value for the angle.")
    sys.exit(1)
