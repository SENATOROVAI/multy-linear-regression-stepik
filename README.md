#### https://SenatorovAI.com

# Normal Equations Solver for Multy Linear Regression

[![License](https://img.shields.io/badge/license-MIT-brightgreen.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![Website](https://img.shields.io/badge/website-live-blue.svg)](https://senatorovai.github.io/Normal-equation-solver-multiple-linear-regression-course/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18818738.svg)](https://doi.org/10.5281/zenodo.18820271)
[![Code Style](https://img.shields.io/badge/code%20style-black-black)]()
[![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen)]()

A research-oriented implementation of the **Normal Equations method** for solving the Multiple Linear Regression problem in closed form.

---

## Overview

This repository provides a mathematically explicit implementation of the Normal Equations approach for solving the least squares problem:

$$
\min_{\beta} \|X\beta - y\|_2^2
$$

The closed-form solution is given by:

$$
\hat{\beta} = (X^T X)^{-1} X^T y
$$

where:

- $X \in \mathbb{R}^{n \times p}$ is the design matrix  
- $y \in \mathbb{R}^n$ is the target vector  
- $\beta \in \mathbb{R}^p$ is the parameter vector  

---

## Mathematical Derivation

The objective function is:

$$
J(\beta) = (X\beta - y)^T (X\beta - y)
$$

Taking the gradient with respect to $\beta$:

$$
\nabla_\beta J = 2 X^T (X\beta - y)
$$

Setting the gradient to zero:

$$
X^T X \beta = X^T y
$$

Assuming $X^T X$ is invertible:

$$
\beta^* = (X^T X)^{-1} X^T y
$$

---

## Assumptions

The Normal Equations require:

$$
\text{rank}(X) = p
$$

so that:

$$
\det(X^T X) \neq 0
$$

Otherwise, the matrix is singular and the solution is not uniquely defined.

---

## Features

- Explicit matrix-based implementation
- Minimal NumPy dependencies
- Research-friendly structure
- Suitable for educational use
- Fully reproducible closed-form solver

---

## Installation

```bash
git clone https://github.com/USERNAME/Normal-equations-solver-multiple-linear-regression.git
cd Normal-equations-solver-simple-linear-regression
pip install -r requirements.txt


