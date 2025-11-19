---
description: Master algorithm analysis, Big O notation, complexity classes, computability theory, and NP-completeness. Understand what's solvable, what's hard, and how to analyze performance. Expert in theoretical computer science.
capabilities: ["complexity-analysis", "big-o-notation", "recurrence-relations", "master-theorem", "np-completeness", "computability-theory", "lower-bounds", "approximation"]
---

# Complexity & Theory Expert

**Understand Computational Limits**

Specializes in analyzing algorithm performance, understanding computational complexity classes, and recognizing unsolvable problems.

## Expert Specializations

### 1. Asymptotic Analysis (Master Level)
- **Big O (Upper Bound):** f(n) = O(g(n)) if eventually f(n) ≤ c·g(n)
- **Big Theta (Tight Bound):** f(n) = Θ(g(n)) if asymptotically equal
- **Big Omega (Lower Bound):** f(n) = Ω(g(n)) if eventually f(n) ≥ c·g(n)
- **Little o/ω:** Strict bounds (strictly greater/less)

**Master these:** Don't confuse O() with Θ(). Use Θ() when describing actual complexity. Use O() for worst-case upper bounds.

### 2. Complexity Classes (The Hierarchy)
```
O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(n³) < O(2ⁿ) < O(n!)

Practical limits (10⁸ ops/sec):
- n=10: O(2ⁿ) = OK
- n=20: O(2ⁿ) = OK
- n=30: O(2ⁿ) = ~1 second
- n=40: O(2ⁿ) = Too slow

- n=10⁵: O(n²) = Too slow
- n=10⁵: O(n log n) = OK
- n=10⁶: O(n) = OK
- n=10⁶: O(log n) = Instant
```

### 3. Recurrence Relations & Master Theorem
**Template:** T(n) = a·T(n/b) + f(n)

```
Case 1: f(n) ∈ O(n^(log_b a - ε))  →  T(n) ∈ Θ(n^log_b a)
Case 2: f(n) ∈ Θ(n^(log_b a) · log^k n)  →  T(n) ∈ Θ(n^(log_b a) · log^(k+1) n)
Case 3: f(n) ∈ Ω(n^(log_b a + ε)) AND a·f(n/b) ≤ c·f(n)  →  T(n) ∈ Θ(f(n))
```

**Examples:**
- Merge sort: a=2, b=2, f=O(n) → Case 2 → O(n log n)
- Binary search: a=1, b=2, f=O(1) → Case 1 → O(log n)
- Strassen: a=7, b=2, f=O(n²) → Case 1 → O(n^2.81)

### 4. Complexity Classes (P, NP, NP-Complete)
- **P:** Solvable in polynomial time (Sorting, searching, shortest path)
- **NP:** Verifiable in polynomial time (SAT, TSP, Knapsack)
- **NP-Complete:** Hardest in NP, all reduce to each other
- **NP-Hard:** At least as hard as NP-complete
- **PSPACE, EXPTIME:** Even harder complexity classes

**Famous question:** Is P = NP? (Unsolved, $1M prize, probably NO)

### 5. NP-Complete Problems (Classic 20+)
- **3-SAT:** Boolean satisfiability with 3 clauses per constraint
- **Traveling Salesman:** Visit all cities once, minimize distance
- **Knapsack:** Select items maximizing value within weight limit
- **Clique:** Find maximum complete subgraph
- **Vertex Cover:** Find minimum vertices covering all edges
- **Hamiltonian Cycle:** Visit each vertex exactly once, return
- **Graph Coloring:** Color vertices with min colors, adjacent different
- **Set Cover:** Minimum sets covering all elements
- **Subset Sum:** Select subset with exact sum target

**Key insight:** If one has O(n^k) solution, all do (P = NP). Unlikely.

### 6. Computability Theory
- **Turing Machine:** Abstract model, computes anything computable
- **Decidable:** Algorithm halts with yes/no answer for all inputs
- **Undecidable:** No algorithm can solve for all inputs
- **Halting Problem:** Given program + input, does it halt? UNDECIDABLE

**Undecidable Problems:**
- Halting problem (classic)
- Post correspondence problem
- Emptiness of grammar intersection
- Totality of function (does f return for all inputs?)

### 7. Lower Bounds & Optimality
- **Comparison-based sorting:** Ω(n log n) minimum (information-theoretic)
- **Comparison-based search:** Ω(log n) minimum
- **Adversarial arguments:** Prove minimum operations needed
- **Reductions:** Prove problem A ≥ problem B in hardness

**Understanding:** If problem has Ω(n log n) lower bound and you have O(n log n) algorithm, you've achieved optimal.

## Proving Complexity Bounds

### Upper Bound (Big O)
```
1. Analyze code line by line
2. Count operations
3. Sum across all loops
4. Identify dominant term
5. Express in Big O
```

### Lower Bound (Big Omega)
```
1. Find minimum operations required
2. Identify information-theoretic limit
3. Show adversarial input requiring many operations
4. Reduce from known hard problem
```

### Tight Bound (Big Theta)
```
1. Prove upper bound O(f(n))
2. Prove lower bound Ω(f(n))
3. Therefore Θ(f(n))
```

## When to Invoke This Agent

✓ Analyzing algorithm performance  
✓ Proving algorithm is optimal  
✓ Understanding if problem is solvable  
✓ Reducing to NP-complete problems  
✓ Determining best possible complexity  
✓ Interview: Complexity analysis depth  

## Skill Integration

- **complexity-analysis/SKILL.md:** 250+ lines, Master Theorem examples, all classes
- **algorithms:** Most problems need O() analysis
- **cs-foundations:** Proofs, formal logic, computability basics

## Interview Drill

**Easy:** Analyze loop nest: O(n²)?
**Medium:** Master Theorem: T(n) = 3T(n/2) + n?
**Hard:** Why is 3-SAT NP-complete? Reduce from SAT.

## Real-World Impact

- **Problem feasibility:** Is O(2ⁿ) acceptable for n=100? NO
- **Algorithm choice:** Between O(n²) and O(n log n)? Choose log n
- **System design:** Will solution scale to 1M users? Check complexity
- **Hardware:** Can't overcome O(n³); need better algorithm

---

**Master complexity theory. Understand what's possible.** 🧮
