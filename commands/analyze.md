# /analyze

Analyze algorithm complexity, performance characteristics, and optimization opportunities.

## Quick Usage

```
/analyze [algorithm-name]        → Full analysis
/analyze time [algorithm]        → Time complexity deep dive
/analyze space [algorithm]       → Space complexity breakdown
/analyze compare [alg1] [alg2]   → Head-to-head comparison
/analyze optimize [code]         → Find optimization opportunities
/analyze [time] [limit]          → Estimate feasibility for input size
```

## Complexity Analysis Guide

### Understanding Big O

**What it means:**
- O(n): Linear - doubles when input doubles
- O(n²): Quadratic - 4× when input doubles
- O(n log n): Linearithmic - optimal for comparison sorts
- O(log n): Logarithmic - excellent, few operations
- O(2ⁿ): Exponential - infeasible for n>20

**Practical limits (10⁸ operations/second):**
```
n=100:
  O(n): instant (100 ops)
  O(n log n): instant (665 ops)
  O(n²): 10ms (10,000 ops)
  O(n³): 1 second (1,000,000 ops)
  O(2ⁿ): IMPOSSIBLE

n=1,000:
  O(n): instant (1,000 ops)
  O(n log n): instant (9,965 ops)
  O(n²): 10ms (1,000,000 ops)
  O(n³): 1 second (1,000,000,000 ops) ← borderline
  O(2ⁿ): IMPOSSIBLE

n=1,000,000:
  O(n): 10ms (1,000,000 ops)
  O(n log n): 200ms (19,931,568 ops)
  O(n²): IMPOSSIBLE (1,000,000,000,000 ops)
```

### Analyzing Your Code

**Step 1: Identify loops**
```
for i in range(n):          # O(n) iterations
    for j in range(n):      # O(n) iterations
        operation()         # O(1) operation
        
Result: O(n) × O(n) × O(1) = O(n²)
```

**Step 2: Identify recursion**
```
def fib(n):
    if n ≤ 1: return n
    return fib(n-1) + fib(n-2)

Recurrence: T(n) = T(n-1) + T(n-2)
Analysis: O(2ⁿ) exponential! ← SLOW
```

**Step 3: Identify data structure operations**
```
hash_set.add(x)         # O(1) average
array.search(x)         # O(n) linear scan
sorted_array.search(x)  # O(log n) binary search (if searching)
heap.push(x)            # O(log n)
```

## Algorithm Analysis Examples

### Merge Sort
```
Algorithm:
1. Split array in half: O(1)
2. Recursively sort left: T(n/2)
3. Recursively sort right: T(n/2)
4. Merge two halves: O(n)

Recurrence: T(n) = 2T(n/2) + O(n)

Master Theorem:
a=2, b=2, f(n)=O(n)
log_b(a) = log₂(2) = 1
f(n) = O(n¹) = n^log_b(a)

Result: Case 2 → O(n log n)
```

### Binary Search
```
Algorithm:
1. Check middle: O(1)
2. Recursively search half: T(n/2)

Recurrence: T(n) = T(n/2) + O(1)

Master Theorem:
a=1, b=2, f(n)=O(1)
log_b(a) = 0
f(n) = O(1) > n⁰ = 1 (barely)

Result: Special case → O(log n)
```

### Dynamic Programming (Fibonacci)
```
Recurrence: T(n) = T(n-1) + T(n-2) + O(1)
Naive: O(2ⁿ) exponential (tree of calls)
Memoized: O(n) linear (each state computed once)
Tabulated: O(n) with O(n) space
Optimized: O(n) with O(1) space (keep 2 values)
```

## Comparing Algorithms

**Sort comparison:**
```
/analyze compare merge quick

Merge Sort vs Quick Sort:
┌──────────┬─────────────┬──────────────────┐
│ Aspect   │ Merge Sort  │ Quick Sort       │
├──────────┼─────────────┼──────────────────┤
│ Avg Time │ O(n log n)  │ O(n log n)       │
│ Worst    │ O(n log n)  │ O(n²) on sorted  │
│ Space    │ O(n) extra  │ O(log n) stack   │
│ Stable   │ Yes         │ No               │
│ In-place │ No          │ Yes              │
│ Cache    │ Bad         │ Good             │
│ When     │ Stability   │ Average case     │
└──────────┴─────────────┴──────────────────┘

Verdict: Quick sort usually faster (cache), merge sort more predictable.
```

## Space Complexity Analysis

### Array Example
```
def create_matrix(n):
    matrix = [[0] * n for _ in range(n)]  # O(n²) space
    return matrix

Space: O(n²) for 2D array storage
```

### Tree Example
```
def recursive_sum(node):
    if not node: return 0
    return node.val + recursive_sum(node.left) + recursive_sum(node.right)

Space: O(h) where h = height
       For balanced: O(log n)
       For skewed: O(n) worst case
```

## Optimization Strategies

### Reduce Loops
```
Before: O(n²) nested loops checking all pairs
for i in range(n):
    for j in range(i+1, n):
        if arr[i] + arr[j] == target:
            return (i, j)

After: O(n) using hash set
seen = set()
for i, num in enumerate(arr):
    complement = target - num
    if complement in seen:
        return (i, j)
    seen.add(num)
```

### Better Data Structure
```
Before: O(n) searching in array
index = arr.index(x)

After: O(1) with hash set
if x in hash_set:
    ...
```

### Parallel Computing
```
Can parallelize some O(n²) work across P processors
Result: O(n²/P) time + synchronization overhead
Practical: Usually 4-8× speedup on 8-core CPU
```

## Common Mistakes

**❌ Forgetting coefficient in loop:**
```
for i in range(n):
    for j in range(i, n):  # Not n times, ~n/2 times
        ...
Analysis: O(n²/2) → still O(n²)
```

**❌ Misunderstanding hash complexity:**
```
for x in set:       # O(n) to iterate all
    if x in set:    # O(1) per check
# Total: O(n) not O(1)
```

**❌ Integer overflow:**
```
mid = (left + right) // 2  # Can overflow!
mid = left + (right - left) // 2  # Safe
```

## Tools & Resources

- **Big-O Cheat Sheet:** Visual complexity guide
- **Wolfram Alpha:** Recurrence relation solver
- **Online Judge:** Submit and get runtime feedback
- **Profiler:** Measure actual code performance

## When to Optimize

**Rule of thumb:**
1. Measure first (profiling)
2. Optimize bottlenecks only
3. Don't premature optimize
4. Verify improvement is real

**Usually:**
- Algorithm choice matters most (10-1000× differences)
- Implementation details matter less (1-10× differences)
- Hardware matters least for small inputs

---

**Analyze before you code. Choose the right algorithm.** 📊
