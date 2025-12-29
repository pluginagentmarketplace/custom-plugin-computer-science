# Complexity Theory Guide

## Complexity Class Hierarchy

```
┌─────────────────────────────────────────┐
│                EXPTIME                   │
│  ┌───────────────────────────────────┐  │
│  │            PSPACE                  │  │
│  │  ┌─────────────────────────────┐  │  │
│  │  │           NP                 │  │  │
│  │  │  ┌───────────────────────┐  │  │  │
│  │  │  │    NP-Complete        │  │  │  │
│  │  │  └───────────────────────┘  │  │  │
│  │  │  ┌───────────────────────┐  │  │  │
│  │  │  │         P             │  │  │  │
│  │  │  └───────────────────────┘  │  │  │
│  │  └─────────────────────────────┘  │  │
│  └───────────────────────────────────┘  │
└─────────────────────────────────────────┘
```

## P vs NP

**P (Polynomial Time)**
- Problems solvable in polynomial time
- Examples: Sorting, Shortest Path, MST

**NP (Non-deterministic Polynomial)**
- Problems verifiable in polynomial time
- Examples: SAT, Hamiltonian Path

**The Million Dollar Question**
> Does P = NP?

If P = NP, every verifiable problem is efficiently solvable.

## NP-Complete Problems

### 3-SAT
```
(x₁ ∨ x₂ ∨ ¬x₃) ∧ (¬x₁ ∨ x₃ ∨ x₄) ∧ ...
Find: Assignment making all clauses true
```

### Vertex Cover
```
Given: Graph G = (V, E), integer k
Find: Set S ⊆ V, |S| ≤ k, covering all edges
```

### Traveling Salesman (Decision)
```
Given: Cities, distances, bound B
Question: Is there a tour of length ≤ B?
```

## Reductions

```python
# Polynomial-time reduction A ≤p B
def reduce_3sat_to_clique(formula):
    """
    If we can solve CLIQUE in poly-time,
    we can solve 3-SAT in poly-time.
    """
    # Build graph from formula
    # If graph has k-clique, formula is satisfiable
    pass
```

## Proving NP-Completeness

1. Show problem is in NP (verifiable in poly-time)
2. Reduce known NP-Complete problem to it
3. Reduction must be polynomial-time

## Dealing with NP-Hard Problems

| Approach | Trade-off |
|----------|-----------|
| Approximation | Near-optimal solution |
| Heuristics | No guarantee, often good |
| Parameterized | Exponential only in parameter |
| Randomized | Probabilistic correctness |

---

*Computer Science Plugin - Theory Skill*
