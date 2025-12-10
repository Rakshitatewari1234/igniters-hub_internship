def solve_expression(exp):
    """Evaluate the mathematical expression safely."""
    exp = exp.replace("^", "**")  # Convert power operator

    try:
        return eval(exp)
    except Exception:
        return "Invalid Expression"

def main():
    input_file = "input.txt"
    output_file = "output.txt"

    try:
        with open(input_file, "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        print("Error: input.txt file not found.")
        return

    with open(output_file, "w") as file:
        for line in lines:
            expression = line.split("=")[0].strip()
            answer = solve_expression(expression)
            file.write(f"{expression} = {answer}\n")

    print("✔ Output written to output.txt")

if __name__ == "__main__":
    main()