---
name: analyze
description: Analyze algorithm complexity and find optimization opportunities
allowed-tools: Read
sasmp_version: "1.3.0"
---

# /analyze

Analyze algorithm complexity, performance, and optimization opportunities.

## Command Schema

```yaml
command_config:
  version: "1.0.0"

  input_validation:
    target:
      type: string
      description: "Algorithm name or code snippet"
      required: true
    analysis_type:
      type: string
      enum: [time, space, both, compare, optimize]
      default: both
    limit:
      type: integer
      description: "Input size for feasibility check"

  exit_codes:
    0: success
    1: unknown_algorithm
    2: invalid_code
    3: analysis_inconclusive
```

## Quick Usage

```
/analyze merge-sort         # Full complexity analysis
/analyze time binary-search # Time complexity focus
/analyze space recursion    # Space complexity focus
/analyze compare merge quick # Head-to-head comparison
/analyze optimize [code]    # Find optimizations
/analyze feasibility 1000000 # Can we handle n=10^6?
```

---

## Complexity Quick Reference

| Notation | Name | Example | n=10^6 time |
|----------|------|---------|-------------|
| O(1) | Constant | Array access | Instant |
| O(log n) | Logarithmic | Binary search | Instant |
| O(n) | Linear | Linear scan | 10ms |
| O(n log n) | Linearithmic | Merge sort | 200ms |
| O(n²) | Quadratic | Nested loops | Impossible |
| O(2ⁿ) | Exponential | Subsets | Impossible |

---

## Analysis Methods

### Count Operations

```python
for i in range(n):          # O(n)
    for j in range(n):      # O(n)
        operation()         # O(1)
# Total: O(n) × O(n) × O(1) = O(n²)
```

### Master Theorem

For T(n) = a·T(n/b) + f(n):

| Case | Condition | Result |
|------|-----------|--------|
| 1 | f(n) < n^log_b(a) | O(n^log_b(a)) |
| 2 | f(n) = n^log_b(a) | O(n^log_b(a) · log n) |
| 3 | f(n) > n^log_b(a) | O(f(n)) |

---

## Algorithm Comparison

```
/analyze compare merge quick

┌──────────┬─────────────┬──────────────────┐
│ Aspect   │ Merge Sort  │ Quick Sort       │
├──────────┼─────────────┼──────────────────┤
│ Avg Time │ O(n log n)  │ O(n log n)       │
│ Worst    │ O(n log n)  │ O(n²)            │
│ Space    │ O(n)        │ O(log n)         │
│ Stable   │ Yes         │ No               │
│ In-place │ No          │ Yes              │
└──────────┴─────────────┴──────────────────┘
```

---

## Optimization Strategies

### Reduce Loops

```python
# Before: O(n²)
for i in range(n):
    for j in range(i+1, n):
        if arr[i] + arr[j] == target:
            return (i, j)

# After: O(n) with hash set
seen = {}
for i, num in enumerate(arr):
    if target - num in seen:
        return (seen[target-num], i)
    seen[num] = i
```

### Better Data Structure

| Before | After | Improvement |
|--------|-------|-------------|
| Array search O(n) | Hash set O(1) | n× faster |
| Nested loops O(n²) | Sorting O(n log n) | n/log n× faster |

---

## Feasibility Check

```
/analyze feasibility 1000000

For n = 1,000,000:
✓ O(log n): ~20 operations - OK
✓ O(n): 1M operations - OK (10ms)
✓ O(n log n): 20M operations - OK (200ms)
✗ O(n²): 10^12 operations - TOO SLOW
✗ O(2^n): Impossible
```

---

## Common Mistakes

| Mistake | Example | Fix |
|---------|---------|-----|
| Hidden loops | str + str in loop | Use StringBuilder |
| Integer overflow | (l+r)/2 | l + (r-l)/2 |
| Hash worst case | All collisions | Better hash function |

---

**Analyze before you code. Choose the right algorithm.**
