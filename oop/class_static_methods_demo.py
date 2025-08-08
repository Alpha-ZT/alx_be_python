class Calculator:
    # Class attribute
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """Static method: Adds two numbers without needing class or instance data."""
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """Class method: Accesses class attribute before multiplying."""
        print(f"Calculation type: {cls.calculation_type}")
        return a * b