# app/history.py
import pandas as pd
import os

class HistoryManager:
    def __init__(self, file_path='calculation_history.csv'):
        self.file_path = file_path
        self.columns = ['Operation', 'Operand1', 'Operand2', 'Result']
        self.history = pd.DataFrame(columns=self.columns)

        if os.path.exists(self.file_path):
            self.load_history()

    def add_record(self, operation, a, b, result):
        next_index = len(self.history)
        self.history.loc[next_index] = [operation, a, b, result]

    def save_history(self):
        self.history.to_csv(self.file_path, index=False)

    def load_history(self):
        self.history = pd.read_csv(self.file_path)

    def clear_history(self):
        self.history = pd.DataFrame(columns=self.columns)
        self.save_history()

    def get_history(self):
        return self.history
