size = 20  # Table size

# Print column headers
print("     ", end="")  # Top-left corner space
for col in range(1, size + 1):
    print(f"{col:4}", end="")
print()

# Print separator line
print("     " + "----" * size)

# Print rows with row headers and multiplication results
for row in range(1, size + 1):
    print(f"{row:3} |", end="")  # Row header
    for col in range(1, size + 1):
        print(f"{row * col:4}", end="")
    print()