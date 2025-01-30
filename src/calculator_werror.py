from typing import Self

class Calculator:
    """A simple calculator supporting basic operations."""

    def __init__(self, x: int, y: str) -> None:# 敢えてyをstr型に変更してエラーを発生させる
        self.x = x
        self.y = y

    def add(self) -> int:
        """Returns the sum of x and y."""
        return self.x + self.y

    def subtract(self) -> int:
        """Returns the difference (x - y)."""
        return self.x - self.y

    def multiply(self) -> int:
        """Returns the product of x and y."""
        return self.x * self.y

    def divide(self) -> float:
        """Returns the result of x / y. Raises an error if y is zero."""
        if self.y == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")
        return self.x / self.y

    def set_values(self, x: int, y: int) -> Self:
        """Updates x and y values and returns the instance."""
        self.x = x
        self.y = y
        return self
