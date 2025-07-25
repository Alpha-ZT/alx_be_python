def perform_operation(num1: float, num2: float, operation: str):
    operation = operation.strip().lower()

    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2

    # Fallback if operation is not one of the expected ones
    return "Invalid operation"
