# /analyze

Analyze algorithm complexity, performance, and correctness. Understand the theoretical and practical performance characteristics.

## Usage

```
/analyze [algorithm-name]
/analyze time-complexity [code]
/analyze space-complexity [code]
/analyze [problem] approach
```

## Examples

```
/analyze merge-sort
Analyze merge sort: complexity, properties, when to use

/analyze time-complexity bubble-sort
Detailed time complexity analysis of bubble sort

/analyze binary-search tradeoffs
Discuss binary search vs linear search trade-offs

/analyze quicksort worst-case
Understand quicksort worst-case behavior and mitigation
```

## Complexity Analysis Guide

### Time Complexity

**Count Operations**
1. Identify primitive operations
2. Count operations in loops
3. Sum up total
4. Find dominant term
5. Express in Big O notation

**Recurrence Relations**
```
T(n) = a·T(n/b) + f(n)

Solve using:
- Substitution method
- Recursion tree
- Master Theorem
```

**Master Theorem**
```
Case 1: f(n) < n^log_b(a)  →  O(n^log_b(a))
Case 2: f(n) = n^log_b(a)  →  O(n^log_b(a) log n)
Case 3: f(n) > n^log_b(a)  →  O(f(n))
```

### Space Complexity

**Count Memory Usage**
1. Input space
2. Auxiliary space (extra)
3. Output space
4. Recursion stack depth

**Example Analysis**
```
Merge Sort:
- Input: O(n)
- Auxiliary: O(n) for temp arrays
- Stack: O(log n) for recursion
- Total: O(n)
```

## Common Algorithm Analysis

### Sorting Algorithms

| Algorithm | Best | Average | Worst | Space | Stable |
|-----------|------|---------|-------|-------|--------|
| Bubble | O(n) | O(n²) | O(n²) | O(1) | Yes |
| Insertion | O(n) | O(n²) | O(n²) | O(1) | Yes |
| Merge | O(n log n) | O(n log n) | O(n log n) | O(n) | Yes |
| Quick | O(n log n) | O(n log n) | O(n²) | O(log n) | No |
| Heap | O(n log n) | O(n log n) | O(n log n) | O(1) | No |
| Counting | O(n+k) | O(n+k) | O(n+k) | O(k) | Yes |

### Search Algorithms

| Algorithm | Time | Space | Conditions |
|-----------|------|-------|------------|
| Linear | O(n) | O(1) | Any array |
| Binary | O(log n) | O(1) | Sorted array |
| Hash | O(1) avg | O(n) | Hash table |
| BST | O(log n) | O(1) | Balanced tree |

### Data Structure Operations

| Structure | Access | Search | Insert | Delete | Space |
|-----------|--------|--------|--------|--------|-------|
| Array | O(1) | O(n) | O(n) | O(n) | O(n) |
| Linked List | O(n) | O(n) | O(1)* | O(1)* | O(n) |
| BST | O(log n) | O(log n) | O(log n) | O(log n) | O(n) |
| Hash Table | - | O(1) avg | O(1) avg | O(1) avg | O(n) |
| Heap | O(n) | O(n) | O(log n) | O(log n) | O(n) |

## Analyzing Your Code

### Step 1: Identify Loops
```
for i in 1 to n:        // O(n)
    for j in 1 to n:    // O(n)
        operation()     // O(1)
```
Nested loops: O(n) × O(n) = O(n²)

### Step 2: Identify Recursion
```
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
```
Recurrence: T(n) = T(n-1) + T(n-2)
Solution: O(2ⁿ)

### Step 3: Identify Data Structure Operations
```
hash_set.add(x)      // O(1) average
sorted_list.search() // O(log n) or O(n)
heap.push()          // O(log n)
```

### Step 4: Combine
- Sequential: Add complexities
- Nested: Multiply complexities
- Conditional: Take maximum
- Recursion: Solve recurrence

## Analysis Patterns

### Binary Search Pattern
```
T(n) = T(n/2) + O(1)
Master Theorem Case 2: O(log n)
```

### Merge Sort Pattern
```
T(n) = 2·T(n/2) + O(n)
Master Theorem Case 2: O(n log n)
```

### Fibonacci Pattern
```
T(n) = T(n-1) + T(n-2)
Solution: O(2ⁿ) → optimize with DP to O(n)
```

## Worst vs Average Case

**Worst Case**: Critical for:
- Guarantees needed
- Real-time systems
- Safety-critical code

**Average Case**: Practical for:
- Typical scenarios
- Real-world performance
- Benchmarking

## Practical Complexity

```
Operation per second: ~10⁸ operations

n=10:         No limit
n=100:        10⁸ ÷ 10⁴ ≈ 10,000 operations ok
n=10⁴:        100 operations max (O(n²) barely works)
n=10⁶:        100 operations max (need O(n log n))
n=10⁸:        10 operations max (need O(1) or O(log n))
```

## Interview Questions

- Analyze time complexity of: [code snippet]
- Solve recurrence: T(n) = 2T(n/2) + n
- Compare binary search vs hash table
- Worst case for quicksort? How to avoid?
- Design algorithm with O(n log n) time
- Prove lower bound for comparison sort
- Optimize this algorithm
- Trade-off between time and space

## Tools & Resources

- Big O Cheat Sheet
- Time Complexity Visualizer
- Recursion Tree Calculator
- CLRS: Introduction to Algorithms
- MIT 6.006: Analysis section

## Next Steps

1. Choose an algorithm to analyze
2. Count operations step by step
3. Express in Big O notation
4. Verify with examples
5. Compare to other algorithms
6. Discuss trade-offs
7. Consider optimization opportunities
