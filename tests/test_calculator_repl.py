# tests/test_calculator_repl.py

import builtins
import pytest
from unittest.mock import patch
from app.calculator_repl import repl

@pytest.mark.parametrize("user_inputs", [
    (["help", "exit"]),
    (["add 5 3", "history", "exit"]),
    (["subtract 10 4", "undo", "redo", "exit"]),
    (["multiply 2 3", "clear", "exit"]),
    (["divide 6 2", "exit"]),
    (["power 2 3", "exit"]),
    (["root 16 2", "exit"]),
    (["unknown 1 2", "exit"]),
    (["add a b", "exit"]),  # Invalid input
])
def test_repl_commands(user_inputs):
    inputs = iter(user_inputs)

    with patch.object(builtins, 'input', lambda _: next(inputs)):
        try:
            repl()  # Call the REPL
        except StopIteration:
            pass  # Ends input simulation
