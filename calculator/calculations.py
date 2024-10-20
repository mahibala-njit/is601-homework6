from typing import List
from calculator.calculation import Calculation
import logging

# Set up logging for this module
logger = logging.getLogger(__name__)

class Calculations:
    """A class to manage a history of mathematical calculations. It allows adding 
    calculations to the history, retrieving the last calculation, and clearing 
    the history"""

    history: List[Calculation] = []

    @classmethod
    def add_calculation(cls, calculation: Calculation):
        """Add a new calculation to the history."""
        cls.history.append(calculation)
        logger.info("Added calculation to history: %s", calculation)

    @classmethod
    def get_last_calculation(cls) -> Calculation:
        """Get the latest calculation. Returns None if there's no history."""
        if cls.history:
            last_calculation = cls.history[-1]
            logger.info("Retrieved last calculation: %s", last_calculation)
            return last_calculation
        logger.warning("No calculations in history to retrieve.")
        return None

    @classmethod
    def get_history(cls) -> List[Calculation]:
        """Gets the entire history of calculations."""
        logger.debug("Retrieving calculation history: %s", cls.history)
        return cls.history

    @classmethod
    def clear_history(cls): 
        """Clears the calculation history."""
        cls.history.clear()
        logger.info("Cleared calculation history.")
