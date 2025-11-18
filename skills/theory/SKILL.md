---
name: complexity-analysis
description: Analyze algorithm complexity, understand Big O notation, computability theory, NP-completeness, and computational limits.
---

# Complexity Analysis & Theory

## Quick Start

Scientifically measure algorithm performance and understand computational limits.

### Asymptotic Notation

**Big O (Upper Bound)**
- f(n) = O(g(n)) if f(n) ≤ c·g(n) eventually
- Describes worst-case behavior
- Example: Insertion sort is O(n²)

**Theta (Tight Bound)**
- f(n) = θ(g(n)) if c₁·g(n) ≤ f(n) ≤ c₂·g(n)
- Exact growth rate
- Example: Merge sort is θ(n log n)

**Omega (Lower Bound)**
- f(n) = Ω(g(n)) if f(n) ≥ c·g(n) eventually
- Describes best-case behavior
- Example: Search is Ω(1) best case

### Common Complexity Classes

```
O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(n³) < O(2ⁿ) < O(n!)
```

## Complexity Analysis Methods

**1. Count Operations**
- Count primitive operations
- Sum up total
- Express as function of n

**2. Recurrence Relations**
- Recursive: T(n) = a·T(n/b) + f(n)
- Solve using:
  - Substitution method
  - Recursion tree
  - Master Theorem

**3. Master Theorem**
```
For T(n) = a·T(n/b) + f(n):

Case 1: f(n) < n^log_b(a)     →  T(n) = O(n^log_b(a))
Case 2: f(n) = n^log_b(a)     →  T(n) = O(n^log_b(a) · log n)
Case 3: f(n) > n^log_b(a)     →  T(n) = O(f(n))
```

## Complexity Classes

**P (Polynomial)**
- Solvable in polynomial time
- Examples: Sorting, shortest path, MST

**NP (Nondeterministic Polynomial)**
- Solutions verifiable in polynomial time
- Includes P
- Examples: SAT, TSP, knapsack

**NP-Complete**
- Hardest in NP
- If one solved in P, all can be
- Examples: 3-SAT, clique, vertex cover

**NP-Hard**
- At least as hard as NP-complete
- May not be verifiable in polynomial time
- Examples: TSP optimization, graph coloring

## Computability Theory

**Turing Machine**
- Abstract model of computation
- Can compute any computable function
- Church-Turing thesis: intuitive algorithm = Turing computable

**Decidability**
- Decidable: algorithm always halts with answer
- Undecidable: no algorithm exists
- Examples: Halting problem, Post correspondence problem

**Reductions**
- Prove problem A ≤ problem B
- If B is hard, so is A
- Tool for proving NP-hardness

## Practical Complexity

| Complexity | Size n | Algorithm |
|------------|--------|-----------|
| O(log n) | 10⁸ | Binary search |
| O(n) | 10⁷ | Linear scan |
| O(n log n) | 10⁶ | Good sort |
| O(n²) | 10⁴ | Slow sort |
| O(n³) | 500 | Triple loop |
| O(2ⁿ) | 20 | Exponential |

## Analysis Perspective

**Worst Case**
- Maximum operations needed
- What you should assume for interviews
- Important for reliability

**Average Case**
- Expected operations (requires probability)
- Real-world performance
- Often matches worst case

**Amortized**
- Average over sequence of operations
- Important for data structures

## NP-Complete Problems

Famous examples:
- **3-SAT**: Boolean satisfiability
- **TSP**: Traveling salesman
- **Knapsack**: 0/1 knapsack
- **Clique**: Find complete subgraph
- **Vertex cover**: Cover all edges
- **Hamiltonian cycle**: Visit each vertex once

## Approximation Algorithms

When exact solution is NP-hard:

**Approximation Ratio**
- Solution ≤ r × optimal
- r-approximation algorithm

**Examples**
- Vertex cover: 2-approximation
- TSP: (1 + log n)-approximation
- Knapsack: FPTAS

## Lower Bounds

**Adversarial Arguments**
- Prove minimum operations needed
- Example: Comparison sort needs Ω(n log n)

**Information-Theoretic**
- Based on information needed
- Example: Search needs log₂(n) comparisons

**Reduction-Based**
- Prove hardness by reduction
- Inherit difficulty of reduced problem

## Interview Prep

- Master Big O notation
- Explain Master Theorem
- Solve recurrence relations
- Recognize NP-complete problems
- Design approximation algorithms
- Analyze algorithm correctness

## Resources

- CLRS: Algorithms textbook (Chapters 1-8)
- Computational Complexity Theory
- MIT 6.006: Algorithms
- Karp's 21 NP-complete problems
