from calculator.calculations import Calculations 
from calculator.operations import add, subtract, multiply, divide  
from calculator.calculation import Calculation 
from decimal import Decimal 
from typing import Callable 
import logging

# Set up logging for this module
logger = logging.getLogger(__name__)

class Calculator:
    """A simple calculator class providing static methods to perform basic arithmetic operations."""

    @staticmethod
    def _perform_operation(a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]) -> Decimal:
        """Create and perform a calculation, then return the result."""
        logger.debug("Performing operation: %s with a: %s, b: %s", operation.__name__, a, b)
        
        calculation = Calculation.create(a, b, operation)
        logger.info("Created calculation: %s", calculation)

        Calculations.add_calculation(calculation)
        logger.info("Added calculation to history: %s", calculation)

        result = calculation.perform()
        logger.info("Performed operation: %s with result: %s", operation.__name__, result)
        return result

    @staticmethod
    def add(a: Decimal, b: Decimal) -> Decimal:
        """Add two Decimal numbers."""
        logger.debug("Adding: %s + %s", a, b)
        return Calculator._perform_operation(a, b, add)

    @staticmethod
    def subtract(a: Decimal, b: Decimal) -> Decimal:
        """Subtract the second Decimal number from the first."""
        logger.debug("Subtracting: %s - %s", a, b)
        return Calculator._perform_operation(a, b, subtract)

    @staticmethod
    def multiply(a: Decimal, b: Decimal) -> Decimal:
        """Multiply two Decimal numbers."""
        logger.debug("Multiplying: %s * %s", a, b)
        return Calculator._perform_operation(a, b, multiply)
    
    @staticmethod
    def divide(a: Decimal, b: Decimal) -> Decimal:
        """Divide the first Decimal number by the second."""
        logger.debug("Dividing: %s / %s", a, b)
        return Calculator._perform_operation(a, b, divide)
