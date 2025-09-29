# app/calculation.py

from app.operations import (
    AddOperation, SubtractOperation, MultiplyOperation,
    DivideOperation, PowerOperation, RootOperation
)

class OperationFactory:
    """Factory for creating operation instances."""
    @staticmethod
    def get_operation(op_name):
        operations = {
            "add": AddOperation(),
            "subtract": SubtractOperation(),
            "multiply": MultiplyOperation(),
            "divide": DivideOperation(),
            "power": PowerOperation(),
            "root": RootOperation()
        }

        op = op_name.lower()
        if op not in operations:
            raise ValueError(f"Unsupported operation: {op}")
        return operations[op]
