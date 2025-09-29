# app/calculator_memento.py

import pandas as pd

class CalculatorMemento:
    """
    Memento that stores a deep copy of the calculator's history state.
    Used to implement undo/redo functionality.
    """
    def __init__(self, state: pd.DataFrame):
        # Store a deep copy to prevent mutation of the original state
        self._state = state.copy(deep=True)

    def get_saved_state(self):
        """
        Return a deep copy of the saved state to ensure isolation.
        """
        return self._state.copy(deep=True)


class MementoManager:
    """
    Manages undo and redo operations using stacks of CalculatorMementos.
    """
    def __init__(self):
        self._undo_stack = []  # Stores previous states for undo
        self._redo_stack = []  # Stores states for redo

    def save_state(self, state: pd.DataFrame):
        """
        Save the current state to the undo stack.
        Clears the redo stack since a new action was taken.
        """
        self._undo_stack.append(CalculatorMemento(state))
        self._redo_stack.clear()

    def undo(self, current_state: pd.DataFrame):
        """
        Undo the last operation.
        Returns the previous state and a boolean indicating success.

        Note:
        - Requires at least two states on the stack to undo (current + previous).
        - Pops the current state and returns the one before it.
        """
        if len(self._undo_stack) < 2:
            return current_state, False  # Nothing to undo

        # Move current state to redo stack
        self._redo_stack.append(CalculatorMemento(current_state))

        # Remove current state from undo stack
        self._undo_stack.pop()

        # Return previous state (now top of undo stack)
        previous_state = self._undo_stack[-1].get_saved_state()
        return previous_state, True

    def redo(self, current_state: pd.DataFrame):
        """
        Redo the last undone operation.
        Returns the next state and a boolean indicating success.
        """
        if not self._redo_stack:
            return current_state, False

        # Move current state to undo stack
        self._undo_stack.append(CalculatorMemento(current_state))

        # Get next state from redo stack
        next_state = self._redo_stack.pop().get_saved_state()
        return next_state, True
