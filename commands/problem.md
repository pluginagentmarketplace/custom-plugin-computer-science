---
name: problem
description: Solve algorithmic problems with hints, solutions, and explanations
allowed-tools: Read
sasmp_version: "1.3.0"
---

# /problem

Solve algorithmic and data structure problems with expert guidance.

## Command Schema

```yaml
command_config:
  version: "1.0.0"

  input_validation:
    problem_name:
      type: string
      pattern: "^[a-z-]+$"
      required: false
    category:
      type: string
      enum: [arrays, strings, trees, graphs, dp, all]
      required: false
    level:
      type: string
      enum: [easy, medium, hard]
      required: false
    action:
      type: string
      enum: [hint, solution, stats, random]
      required: false

  exit_codes:
    0: success
    1: problem_not_found
    2: invalid_category
    3: hint_exhausted
```

## Quick Usage

```
/problem two-sum           # Get problem statement
/problem two-sum hint      # Progressive hints (1-3 levels)
/problem two-sum solution  # See optimal solution
/problem arrays            # List array problems
/problem arrays easy       # Filter by difficulty
/problem random medium     # Random medium problem
/problem stats             # Your progress statistics
```

---

## Problem Categories (50+)

### Arrays & Sequences (15 problems)

| Level | Problem | Technique |
|-------|---------|-----------|
| Easy | Two Sum | Hash map |
| Easy | Max Subarray | Kadane's |
| Medium | Product Except Self | Prefix/suffix |
| Hard | Trapping Rain Water | DP/Stack |

### Strings & Patterns (12 problems)

| Level | Problem | Technique |
|-------|---------|-----------|
| Easy | Valid Palindrome | Two pointers |
| Medium | Word Break | DP |
| Hard | Regex Matching | DP 2D |

### Trees (15 problems)

| Level | Problem | Technique |
|-------|---------|-----------|
| Easy | Inorder Traversal | Recursion/Stack |
| Medium | LCA | DFS |
| Hard | Serialize Tree | Preorder + markers |

### Graphs (12 problems)

| Level | Problem | Technique |
|-------|---------|-----------|
| Easy | Number of Islands | DFS/BFS |
| Medium | Course Schedule | Topological sort |
| Hard | Network Delay | Dijkstra |

### Dynamic Programming (30 problems)

| Level | Problem | Technique |
|-------|---------|-----------|
| Easy | Fibonacci | Memoization |
| Medium | Knapsack | 2D DP |
| Hard | Burst Balloons | Interval DP |

---

## Solving Framework

1. **Understand:** Read 2-3 times, find edge cases
2. **Plan:** Brute force first, then optimize
3. **Code:** Clean implementation, handle edges
4. **Verify:** Test with examples

---

## Hint System

| Level | Description | Example |
|-------|-------------|---------|
| 1 | Direction | "Consider using a hash set" |
| 2 | Approach | "Use two pointers from opposite ends" |
| 3 | Pseudocode | Algorithm outline with placeholders |

---

## Solution Quality

Each solution includes:
1. **Explanation:** Why this approach works
2. **Complexity:** Time O(?), Space O(?)
3. **Code:** Clean, well-commented
4. **Variations:** Alternative approaches

---

## Difficulty Guide

| Level | Time | Description |
|-------|------|-------------|
| Easy | 5-10 min | Straightforward, one approach |
| Medium | 15-30 min | Pattern not obvious |
| Hard | 30-60 min | Complex, tricky edges |

---

**Start:** `/problem arrays easy` for beginners.
