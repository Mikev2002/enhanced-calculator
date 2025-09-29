# tests/test_history.py

import os
import pandas as pd
from app.history import HistoryManager

def test_add_and_load_history(tmp_path):
    file_path = tmp_path / "test_history.csv"

    # Create first history manager and add a record
    history = HistoryManager(file_path=str(file_path))
    history.add_record("add", 5, 3, 8)
    history.save_history()

    # Create a new instance and load history from file
    new_history = HistoryManager(file_path=str(file_path))
    df = new_history.get_history()
    assert len(df) == 1
    assert df.iloc[0]["Result"] == 8

    # Now clear and verify it's empty
    new_history.clear_history()
    assert new_history.get_history().empty
