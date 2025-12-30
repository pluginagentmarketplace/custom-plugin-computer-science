---
name: complexity-analysis
description: Analyze algorithm complexity, understand Big O notation, computability theory, NP-completeness, and computational limits.
sasmp_version: "1.3.0"
bonded_agent: 04-complexity-theory-expert
bond_type: PRIMARY_BOND
---

# Complexity Analysis Skill

## Skill Metadata

```yaml
skill_config:
  version: "1.0.0"
  category: theoretical
  prerequisites: [cs-foundations, algorithms]
  estimated_time: "4-6 weeks"
  difficulty: advanced

  parameter_validation:
    analysis_type:
      type: string
      enum: [time, space, both]
      default: both
    notation:
      type: string
      enum: [big-o, theta, omega]

  retry_config:
    max_attempts: 3
    backoff_strategy: exponential
    initial_delay_ms: 500

  observability:
    log_level: INFO
    metrics: [analysis_accuracy, master_theorem_usage]
```

---

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

### Common Complexity Classes

```
O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(n³) < O(2ⁿ) < O(n!)
```

---

## Master Theorem

For T(n) = a·T(n/b) + f(n):

```
Case 1: f(n) < n^log_b(a)  →  T(n) = O(n^log_b(a))
Case 2: f(n) = n^log_b(a)  →  T(n) = O(n^log_b(a) · log n)
Case 3: f(n) > n^log_b(a)  →  T(n) = O(f(n))
```

---

## Complexity Classes

**P (Polynomial)**: Solvable in polynomial time
**NP (Nondeterministic Polynomial)**: Solutions verifiable in polynomial time
**NP-Complete**: Hardest in NP
**NP-Hard**: At least as hard as NP-complete

---

## Troubleshooting

| Issue | Root Cause | Resolution |
|-------|------------|------------|
| Wrong Big-O | Hidden loops ignored | Trace all operations |
| Master Theorem fails | Conditions not met | Use substitution method |
| Empirical mismatch | Hidden constants | Count operations precisely |

---

## Practical Complexity

| Complexity | Size n | Algorithm |
|------------|--------|-----------|
| O(log n) | 10⁸ | Binary search |
| O(n) | 10⁷ | Linear scan |
| O(n log n) | 10⁶ | Good sort |
| O(n²) | 10⁴ | Slow sort |
| O(2ⁿ) | 20 | Exponential |

---

## NP-Complete Problems

Famous examples:
- **3-SAT**: Boolean satisfiability
- **TSP**: Traveling salesman
- **Knapsack**: 0/1 knapsack
- **Clique**: Find complete subgraph
- **Vertex cover**: Cover all edges
