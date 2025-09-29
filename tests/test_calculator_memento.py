import pandas as pd
from app.calculator_memento import MementoManager

def test_undo_redo():
    memento = MementoManager()
    columns = ["Operation", "Operand1", "Operand2", "Result"]

    # State 0: empty
    df0 = pd.DataFrame(columns=columns)
    memento.save_state(df0)

    # State 1: add record
    df1 = pd.DataFrame([["add", 1, 2, 3]], columns=columns)
    memento.save_state(df1)

    # State 2: add another record
    df2 = pd.DataFrame([
        ["add", 1, 2, 3],
        ["subtract", 5, 3, 2]
    ], columns=columns)
    memento.save_state(df2)

    # Undo → should go to df1 (1 row)
    new_state, changed = memento.undo(df2)
    assert changed is True
    assert len(new_state) == 1
    assert new_state.iloc[0]["Operation"] == "add"

    # Undo → should go to df0 (empty)
    new_state, changed = memento.undo(new_state)
    assert changed is True
    assert new_state.empty

    # Undo again → nothing to undo
    new_state, changed = memento.undo(new_state)
    assert changed is False

    # Redo → back to df1
    new_state, changed = memento.redo(df0)
    assert changed is True
    assert len(new_state) == 1

    # Redo → back to df2
    new_state, changed = memento.redo(new_state)
    assert changed is True
    assert len(new_state) == 2

    # Redo → nothing left to redo
    new_state, changed = memento.redo(new_state)
    assert changed is False
