---
description: Analyze algorithm complexity, understand Big O notation, computability theory, and complexity classes. Master the mathematical analysis of algorithms.
capabilities: ["big-o-analysis", "complexity-classes", "computability-theory", "np-completeness", "approximation", "lower-bounds"]
---

# Complexity & Theory Expert

Scientifically analyze algorithm performance. Understand computational limits and complexity classes that define what's solvable.

## Asymptotic Analysis

### Big O Notation
- **Definition**: Upper bound on growth rate
- **Example**: f(n) = O(g(n)) if f(n) ≤ c·g(n) for all n ≥ n₀
- **Common Classes**: O(1), O(log n), O(n), O(n log n), O(n²), O(2ⁿ), O(n!)

### Theta Notation (Θ)
- **Definition**: Tight bound, both upper and lower
- **Meaning**: Algorithm grows at exactly this rate
- **Example**: θ(n²) means c₁·n² ≤ f(n) ≤ c₂·n²

### Omega Notation (Ω)
- **Definition**: Lower bound on growth rate
- **Example**: f(n) = Ω(g(n)) if f(n) ≥ c·g(n) for all n ≥ n₀

### Little o and ω
- **Little o**: Strict upper bound (f grows strictly slower)
- **Little ω**: Strict lower bound (f grows strictly faster)

## Time Complexity Analysis

### Methods of Analysis

**1. Count Operations**
- Count primitive operations (arithmetic, comparison, assignment)
- Sum up total operations
- Express as function of input size n

**2. Recurrence Relations**
- Express T(n) in terms of T(n-1), T(n/2), etc.
- Solve using:
  - Substitution method
  - Recursion tree method
  - Master Theorem

**3. Master Theorem**
```
For T(n) = a·T(n/b) + f(n):

Case 1: f(n) = O(n^(log_b(a) - ε))  →  T(n) = Θ(n^log_b(a))
Case 2: f(n) = Θ(n^log_b(a) · log^k(n))  →  T(n) = Θ(n^log_b(a) · log^(k+1)(n))
Case 3: f(n) = Ω(n^(log_b(a) + ε))  →  T(n) = Θ(f(n))
```

## Complexity Classes

### P (Polynomial Time)
- Problems solvable in polynomial time
- Deterministic algorithms
- Examples: Sorting, searching, shortest path

### NP (Nondeterministic Polynomial Time)
- Problems where solutions verifiable in polynomial time
- Includes all P problems
- Examples: SAT, traveling salesman, knapsack

### NP-Complete
- Hardest problems in NP
- If any NP-complete problem is in P, then P = NP
- Famous examples:
  - 3-SAT (Boolean satisfiability)
  - Traveling Salesman Problem
  - Knapsack Problem
  - Clique Problem
  - Vertex Cover
  - Hamiltonian Cycle

### NP-Hard
- At least as hard as NP-complete
- May not be in NP itself
- Examples: Optimization versions of NP-complete problems

### PSPACE, EXPTIME, etc.
- PSPACE: Solvable with polynomial space
- EXPTIME: Solvable in exponential time
- Hierarchy: P ⊆ NP ⊆ PSPACE ⊆ EXPTIME

## Computability Theory

### Turing Machines
- **Abstract Model**: Infinite tape, read/write head, state machine
- **Universality**: Can compute any computable function
- **Church-Turing Thesis**: Intuitive notion of algorithm = Turing computable

### Decidability
- **Decidable**: Algorithm exists that always halts with yes/no
- **Undecidable**: No algorithm can solve in finite time
- **Examples of Undecidable**:
  - Halting problem
  - Post correspondence problem
  - Tiling problem

### Reducibility
- **Reduction**: Transform problem A into problem B
- **Purpose**: Prove hardness by showing problem B is at least as hard as A
- **Example**: Reduce SAT to 3-SAT to prove 3-SAT NP-hard

## Lower Bounds

### Adversarial Arguments
- Prove minimum operations needed
- Example: Any comparison-based sort needs Ω(n log n)

### Information-Theoretic Bounds
- Example: Finding element in n elements needs log₂(n) bits of information

### Reduction-Based Lower Bounds
- Reduce from known hard problem
- Inherit difficulty of reduced problem

## Approximation Algorithms

When exact solution is NP-hard:

### Approximation Ratio
- **Definition**: Ratio of approximate solution to optimal
- **Example**: Factor-2 approximation means solution ≤ 2 × optimal

### Common Approximations
- **Vertex Cover**: Factor-2 greedy algorithm
- **Knapsack**: FPTAS (Fully polynomial-time approximation)
- **TSP**: Factor-(1 + log n) using MST

### Inapproximability
- Some problems cannot be approximated beyond certain ratio
- Unless P = NP

## Practical Complexity Guide

| Class | Size n | Algorithm |
|-------|--------|-----------|
| O(log n) | 10⁸ | Binary search |
| O(n) | 10⁸ | Linear scan |
| O(n log n) | 10⁷ | Merge sort |
| O(n²) | 10⁴ | Nested loops |
| O(n³) | 500 | Triple nested loops |
| O(2ⁿ) | 20 | Exponential |
| O(n!) | 10 | Factorial |

## Analysis Techniques

1. **Worst Case**: Maximum operations needed
2. **Average Case**: Expected operations (requires probability)
3. **Best Case**: Minimum operations (often trivial)
4. **Amortized**: Average over sequence of operations

## Interview Questions

- What's the difference between Big O and Big Theta?
- Master Theorem: Explain the three cases
- Is P = NP? Why does it matter?
- Reduce problem A to B: what does that prove?
- Design a O(n log n) algorithm for...
- What's the lower bound for comparison-based sorting?
- Is this problem NP-complete? How would you prove it?

## Resources

- CLRS: Introduction to Algorithms (Chapters on complexity)
- MIT 6.006: Introduction to Algorithms
- Complexity theory textbooks for deeper understanding
