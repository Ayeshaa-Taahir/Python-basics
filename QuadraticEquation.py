import sys
import math

# Function to solve the quadratic equation
def solve_quadratic(a, b, c):
    discriminant = b**2 - 4*a*c

    print("\nSolving the quadratic equation: ax² + bx + c = 0\n")
    print(f"\tGiven: a = {a}, b = {b}, c = {c}")

    if discriminant < 0:
        print("\n\tNo real roots exist.")
    elif discriminant == 0:
        x = -b / (2 * a)
        print(f"\n\tOnly one real root:\n\t\tx = {x}")
    else:
        sqrt_disc = math.sqrt(discriminant)
        x1 = (-b + sqrt_disc) / (2 * a)
        x2 = (-b - sqrt_disc) / (2 * a)
        print(f"\n\tTwo real roots found:")
        print(f"\t\tx1 = {x1}")
        print(f"\t\tx2 = {x2}")

# Main code block that runs only if the script is run directly
if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage:\n\tpython QuadraticEquation.py a b c")
    else:
        try:
            # Casting command-line arguments to float
            a = float(sys.argv[1])
            b = float(sys.argv[2])
            c = float(sys.argv[3])
            solve_quadratic(a, b, c)
        except ValueError:
            print("\n\tPlease enter valid numeric values for a, b, and c.")