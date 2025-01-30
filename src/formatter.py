class Formatter:
    """A simple formatter for displaying results."""

    @staticmethod
    def format_result(operation: str, result: float | int) -> str:
        """Formats the output result with proper precision."""
        return f"The result of {operation} is: {result:.2f}" if isinstance(result, float) else f"The result of {operation} is: {result}"
