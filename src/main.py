from calculator import Calculator
from formatter import Formatter

def main() -> None:
    """Main function to demonstrate basic calculator operations."""
    # Create a calculator instance and perform basic operations
    print("Creating a calculator instance and performing basic operations...")
    calc = Calculator(10, 5)
    formatter = Formatter()

    results = {
        "addition": calc.add(),
        "subtraction": calc.subtract(),
        "multiplication": calc.multiply(),
        "division": calc.divide()
    }

    for operation, result in results.items():
        print(formatter.format_result(operation, result))

    # Demonstrate error handling
    print("Creating a calculator instance with mypy error...")
    calc_with_error = Calculator(10, 5)
    formatter_with_error = Formatter()
    
    results_with_error = {
        "addition": calc_with_error.add(),
        "subtraction": calc_with_error.subtract(),
        "multiplication": calc_with_error.multiply(),
        "division": calc_with_error.divide()
    }
    
    for operation, result in results_with_error.items():
        print(formatter_with_error.format_result(operation, result))
        

if __name__ == "__main__":
    main()
