# app/calculator_repl.py

# Author: Mike V.
# Date: 2025-09-29
# Enhanced Calculator - Module 5 Assignment


from app.calculation import OperationFactory
from app.history import HistoryManager
from app.calculator_memento import MementoManager

def repl():
    print("Welcome to the Enhanced Calculator!")
    print("Type 'help' for commands, 'exit' to quit.")

    history = HistoryManager()
    mementos = MementoManager()
    mementos.save_state(history.get_history())  # Save initial empty state

    while True:
        user_input = input(">>> ")

        if user_input.strip() == "":
            continue

        command = user_input.lower()

        # === Commands ===
        if command == "exit":
            history.save_history()
            print("Goodbye!")
            break

        elif command == "help":
            print("Available operations:")
            print("  add, subtract, multiply, divide, power, root")
            print("Commands:")
            print("  history   → show past calculations")
            print("  clear     → clear history")
            print("  undo      → undo last calculation")
            print("  redo      → redo last undone calculation")
            print("  exit      → quit and save")
            continue

        elif command == "history":
            df = history.get_history()
            if df.empty:
                print("No history yet.")
            else:
                print(df.to_string(index=False))
            continue

        elif command == "clear":
            history.clear_history()
            mementos.save_state(history.get_history())
            print("History cleared.")
            continue

        elif command == "undo":
            new_state, changed = mementos.undo(history.get_history())
            if changed:
                history.history = new_state.copy(deep=True)
                print("Undo successful.")
            else:
                print("Nothing to undo.")
            continue

        elif command == "redo":
            new_state, changed = mementos.redo(history.get_history())
            if changed:
                history.history = new_state.copy(deep=True)
                print("Redo successful.")
            else:
                print("Nothing to redo.")
            continue

        # === Handle calculations ===
        parts = user_input.strip().split()
        if len(parts) != 3:
            print("Invalid input format. Use: operation operand1 operand2")
            continue

        operation, a_str, b_str = parts

        try:
            a = float(a_str)
            b = float(b_str)
        except ValueError:
            print("Operands must be valid numbers.")
            continue

        try:
            # Save state BEFORE adding new record so undo works properly
            mementos.save_state(history.get_history())

            op_instance = OperationFactory.get_operation(operation)
            result = op_instance.execute(a, b)
            print(f"Result: {result}")

            history.add_record(operation, a, b, result)
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    repl()
