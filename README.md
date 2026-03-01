# Stepik: https://stepik.org/a/272346

# Limited-Memory BFGS (L-BFGS) solver — A Research-Oriented Course

[![License](https://img.shields.io/badge/license-MIT-brightgreen.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![Website](https://img.shields.io/badge/website-live-blue.svg)](https://senatorovai.github.io/lbfgs-solver-course/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18818738.svg)](https://doi.org/10.5281/zenodo.18818738)

Research-oriented course and implementation of the **L-BFGS / L-BFGS-B quasi-Newton optimization algorithm**.

The project combines:

- Mathematical derivation from first principles
- Convergence theory and Wolfe line search analysis
- Two-loop recursion implementation
- Production-style Python solver
- Large-scale numerical experiments

Designed for researchers, ML engineers, and students studying second-order optimization methods.

---

## Project Status

**Status:** Active development.

Core solver implementation and theoretical documentation are stable.

Future improvements include:

- Extended benchmarking framework
- Additional test coverage
- Performance profiling
- Visualization of convergence dynamics

Contributions are welcome. See `CONTRIBUTING.md` for guidelines.

> A mathematically rigorous course on the **Limited-memory Broyden–Fletcher–Goldfarb–Shanno (L-BFGS)** algorithm, covering theoretical foundations, convergence properties, numerical stability, and large-scale implementations.

---

## Abstract

The Limited-memory BFGS (L-BFGS) method is a quasi-Newton optimization algorithm designed for large-scale unconstrained and box-constrained smooth optimization problems. It achieves superlinear convergence under standard assumptions while requiring only linear memory in the number of variables.

This course presents:

- A full derivation of the BFGS update from the secant condition  
- Proof of positive definiteness preservation  
- Two-loop recursion derivation for L-BFGS  
- Wolfe line-search theory  
- Global convergence analysis  
- Practical implementation details (including L-BFGS-B)

The treatment follows the theoretical framework established in:

- *Numerical Optimization*  
- *Convex Optimization*

---

## Scope

We study smooth optimization problems of the form:

$$
\min_{x \in \mathbb{R}^n} f(x)
$$

where:

- $f \in C^1$ (continuously differentiable),
- $\nabla f$ is Lipschitz continuous,
- optionally $f$ is strongly convex.

Extensions to box constraints:

$$
\min_{l \le x \le u} f(x)
$$

are treated via the L-BFGS-B framework as implemented in:

- SciPy

---

## Theoretical Contributions Covered

### 1. From Newton to Quasi-Newton

- Second-order Taylor approximation  
- Newton direction  
- Limitations of exact Hessian computation  
- Motivation for Hessian approximation  

---

### 2. Secant Condition

We derive the quasi-Newton equation:

$$
B_{k+1}s_k = y_k
$$

where:

$$
s_k = x_{k+1} - x_k, \qquad
y_k = \nabla f(x_{k+1}) - \nabla f(x_k)
$$

We show:

- Why the update must satisfy symmetry  
- Why positive definiteness requires $y_k^T s_k > 0$  
- How the BFGS rank-two update arises from minimal correction principles  

---

### 3. BFGS Update

Derivation:

$$
H_{k+1} =
\left(I - \rho_k s_k y_k^T \right)
H_k
\left(I - \rho_k y_k s_k^T \right)
+
\rho_k s_k s_k^T
$$

with:

$$
\rho_k = \frac{1}{y_k^T s_k}
$$

We prove:

- Symmetry preservation  
- Positive definiteness preservation  
- Superlinear convergence under standard assumptions  

---

### 4. Limited-Memory Formulation

For large $n$, storing $H_k \in \mathbb{R}^{n \times n}$ is infeasible.

L-BFGS stores only the last $m$ curvature pairs:

$$
\{(s_i, y_i)\}_{i=k-m}^{k-1}
$$

The two-loop recursion computes:

$$
p_k = -H_k \nabla f(x_k)
$$

without forming $H_k$ explicitly.

Memory complexity:

$$
O(nm)
$$

Time complexity per iteration:

$$
O(nm)
$$

---

### 5. Line Search Theory

We provide formal treatment of:

- Weak Wolfe conditions  
- Strong Wolfe conditions  
- Curvature condition  
- Global convergence theorems  

Under Wolfe conditions:

$$
y_k^T s_k > 0
$$

which ensures stability of the BFGS update.

---

### 6. Convergence Results

Under:

- Lipschitz continuous gradient  
- Strong convexity  
- Wolfe line search  

BFGS and L-BFGS achieve:

- Global convergence  
- Local superlinear convergence  

We discuss:

- Failure cases in nonconvex problems  
- Saddle point behavior  
- Curvature degeneracy  

---

## Numerical Implementation

The repository contains:

- Pure Python implementation  
- NumPy-based vectorized routines  
- Explicit two-loop recursion  
- Wolfe line-search implementation  
- L-BFGS-B box constraint handling  

Reference comparison with:

- SciPy  
- Original Fortran L-BFGS-B implementation by Nocedal et al.

---

## Repository Structure

```

lbfgs-research/
│
├── theory/
│   ├── newton_method.md
│   ├── secant_condition.md
│   ├── bfgs_proof.md
│   ├── lbfgs_two_loop.md
│   ├── wolfe_conditions.md
│   └── convergence_analysis.md
│
├── implementation/
│   ├── lbfgs.py
│   ├── line_search.py
│   ├── lbfgsb.py
│   └── utils.py
│
├── experiments/
│   ├── quadratic_tests.ipynb
│   ├── logistic_regression.ipynb
│   └── large_scale_benchmark.ipynb
│
└── README.md

````

---

## Experimental Evaluation

We benchmark:

- Quadratic functions (known Hessian)  
- Ill-conditioned problems  
- Logistic regression  
- High-dimensional synthetic datasets  

Metrics:

- Iteration count  
- Gradient norm decay  
- Function value reduction  
- Wall-clock time  

Comparisons include:

- Gradient Descent  
- Newton’s Method  
- Conjugate Gradient  

---

## Prerequisites

- Linear algebra (spectral decomposition, positive definiteness)  
- Multivariable calculus  
- Numerical optimization theory  
- Familiarity with quasi-Newton methods  

---

## Research Applications

L-BFGS is widely used in:

- Statistical estimation  
- Maximum likelihood problems  
- Inverse problems  
- Scientific computing  
- Large-scale machine learning  

Framework adoption includes:

- SciPy  
- PyTorch  
- TensorFlow  

---

## Citation

If you use this repository for academic or research purposes, please cite:

```bibtex
@misc{lbfgs_course,
  author = {Ruslan Senatorov},
  title  = {L-BFGS: Theory, Convergence, and Implementation},
  year   = {2026},
}
````

---

## License

MIT License

