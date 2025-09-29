# Enhanced Calculator 

A modular command-line calculator built in Python, featuring:

-  Advanced arithmetic operations
-  Design patterns: Factory, Strategy, Memento, Observer, Facade
-  pandas-powered calculation history
-  Undo / redo functionality
-  Environment-based configuration
-  100% automated tests with GitHub Actions + Coverage enforcement

---



---

## Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/Mikev2002/enhanced-calculator.git
cd enhanced-calculator


2. Set up your environment

py -m venv venv
venv\Scripts\activate   # Windows
# or
source venv/bin/activate  # macOS/Linux

pip install -r requirements.txt

3. Run the Calculator

$env:PYTHONPATH="."     # Windows (PowerShell)
python app/calculator_repl.py
