# Quick Start

This guide helps you get up and running quickly with the **Normal-equation-solver-multiple-linear-regression-course** project — from installation to running your first optimization.

---

## 🚀 1. Clone the Repository

First, fork the repository (optional) and clone it locally:

```bash
git clone https://github.com/SENATOROVAI/Normal-equation-solver-multiple-linear-regression-course.git
cd Normal-equation-solver-multiple-linear-regression-course
````

---

## 🧠 2. Set Up Python Environment

We recommend using a virtual environment:

### Create and activate:

```bash
python3 -m venv venv
source venv/bin/activate      # macOS / Linux
venv\Scripts\activate         # Windows
```

---

## 📦 3. Install Dependencies

Install required packages:

```bash
pip install -r requirements.txt
```

If you are using a package manager like Poetry:

```bash
poetry install
```

---

## 📁 4. Explore Project Structure

```text
Normal-equation-solver-multiple-linear-regression-course/
│
├── docs/                  # GitHub Pages & documentation
├── theory/                # Mathematical derivations
├── implementation/        # Python solver code
├── experiments/           # Notebooks and benchmarks
├── tests/                 # Test suite
├── README.md
├── QUICKSTART.md
├── LICENSE
└── requirements.txt
```

---

## 🧪 5. Run Your First Example

A minimal usage example with a quadratic objective:

```python
import numpy as np

def f(x):
    return np.sum(x**2)

def grad(x):
    return 2*x

# Initial guess
x0 = np.array([5.0, -3.0, 2.0])

print("Optimal x:", x_opt)
```

Save this as `example.py` and run:

```bash
python example.py
```

---

## 🧰 6. Run Notebooks

You can explore interactive notebooks in the `experiments/` folder:

```bash
jupyter notebook
```

Or with JupyterLab:

```bash
jupyter lab
```

---

## 🚀 7. Run Tests

If you added tests to the repository:

```bash
pytest
```

Ensure all tests pass before submitting PRs.

---

## 📊 8. Run Benchmarks

Benchmark scripts in `experiments/` produce performance graphs:

```bash
python experiments/quadratic_tests.py
```

Add your own benchmarks or compare with SciPy’s solver.

---

## 🎯 9. Tips & Useful Commands

* Check code style:

```bash
black .
flake8 .
```

* Format with:

```bash
isort .
```

---

## ❓ 10. Need Help?

If you run into issues:

✔ Check `TROUBLESHOOTING.md`
✔ Search existing issues
✔ Open a new issue with full description

---

## 🎉 You’re Ready!

You should now be able to:

* Understand solver internals
* Run optimization examples
* Contribute code with confidence

Happy optimizing! 
