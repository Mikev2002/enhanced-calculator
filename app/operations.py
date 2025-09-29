# app/operations.py

from abc import ABC, abstractmethod

class OperationStrategy(ABC):
    @abstractmethod
    def execute(self, a, b):
        pass

class AddOperation(OperationStrategy):
    def execute(self, a, b):
        return a + b

class SubtractOperation(OperationStrategy):
    def execute(self, a, b):
        return a - b

class MultiplyOperation(OperationStrategy):
    def execute(self, a, b):
        return a * b

class DivideOperation(OperationStrategy):
    def execute(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b

class PowerOperation(OperationStrategy):
    def execute(self, a, b):
        return a ** b

class RootOperation(OperationStrategy):
    def execute(self, a, b):
        if b == 0:
            raise ValueError("Cannot take root with zero.")
        return a ** (1 / b)
