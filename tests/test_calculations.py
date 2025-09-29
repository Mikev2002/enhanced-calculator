# tests/test_calculation.py

import pytest
from app.calculation import OperationFactory
from app.operations import AddOperation, SubtractOperation, MultiplyOperation, DivideOperation, PowerOperation, RootOperation

def test_factory_add():
    op = OperationFactory.get_operation("add")
    assert isinstance(op, AddOperation)

def test_factory_subtract():
    op = OperationFactory.get_operation("subtract")
    assert isinstance(op, SubtractOperation)

def test_factory_multiply():
    op = OperationFactory.get_operation("multiply")
    assert isinstance(op, MultiplyOperation)

def test_factory_divide():
    op = OperationFactory.get_operation("divide")
    assert isinstance(op, DivideOperation)

def test_factory_power():
    op = OperationFactory.get_operation("power")
    assert isinstance(op, PowerOperation)

def test_factory_root():
    op = OperationFactory.get_operation("root")
    assert isinstance(op, RootOperation)

def test_factory_invalid_operation():
    with pytest.raises(ValueError):
        OperationFactory.get_operation("invalid_op")
