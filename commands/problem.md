# /problem

Solve algorithmic and data structure problems with expert guidance, hints, and solutions.

## Quick Usage

```
/problem [name]              → Get problem statement and hints
/problem [name] hint         → Progressive hints (1-3 levels)
/problem [name] solution     → See optimal solution + explanation
/problem [category]          → List problems in category
/problem [category] [level]  → Filter by difficulty
/problem random [level]      → Surprise me! (practice)
/problem stats               → Your progress statistics
```

## Problem Categories (50+ problems)

### Arrays & Sequences (15 problems)
```
Level 1:
- Two Sum (find pair with target sum)
- Max Subarray (Kadane's algorithm)
- Duplicate Element (cycle detection)
- Rotate Array (in-place rotation)
- Contains Duplicate (hash set)

Level 2:
- Product of Array Except Self (prefix/suffix)
- Median of Two Sorted Arrays (binary search approach)
- Best Time to Buy Stock (one pass O(n))
- Trapping Rain Water (dynamic programming)
- Next Permutation (in-place generation)

Level 3:
- Largest Rectangle in Histogram (monotonic stack)
- First Missing Positive (in-place array indexing)
- Multiply Strings (bignum arithmetic)
```

### Strings & Patterns (12 problems)
```
Level 1:
- Valid Palindrome (two pointers)
- Longest Common Prefix (column comparison)
- Longest Substring Without Repeating (sliding window)
- Anagrams (sorting or character count)

Level 2:
- Regex Pattern Matching (dynamic programming)
- Word Break (DP or backtracking)
- Edit Distance (DP 2D table)
- Group Anagrams (hash map grouping)

Level 3:
- Wildcard Pattern Matching (greedy + DP)
- KMP Algorithm (string pattern matching)
```

### Trees (15 problems)
```
Level 1:
- Inorder Traversal (recursion, stack)
- Level Order Traversal (BFS queue)
- Path Sum (DFS, target matching)
- Validate BST (recursive verification)

Level 2:
- Lowest Common Ancestor (DFS, backtracking)
- Binary Tree Maximum Path Sum (DP on trees)
- Serialize Deserialize (preorder + markers)
- Flatten Binary Tree (recursion, pointers)

Level 3:
- Recover Binary Search Tree (swapped nodes fix)
- Maximum Path in Tree (hard DP)
```

### Graphs (12 problems)
```
Level 1:
- Number of Islands (DFS/BFS)
- Graph Valid Tree (Union-Find or BFS)
- Course Schedule (Topological sort)

Level 2:
- Shortest Path in Grid (Dijkstra, BFS)
- Alien Dictionary (Topological sort)
- Number of Connected Components (Union-Find)

Level 3:
- Network Delay Time (Dijkstra, shortest path)
- Minimum Spanning Tree (Kruskal, Prim)
```

### Dynamic Programming (30 problems)
```
Level 1:
- Fibonacci (memoization intro)
- Climbing Stairs (simple DP)
- House Robber (max without adjacent)
- Coin Change (min coins)

Level 2:
- Longest Increasing Subsequence (O(n²) or O(n log n))
- Knapsack 0/1 (classic DP)
- Longest Common Subsequence (2D DP)
- Matrix Chain Multiplication (interval DP)

Level 3:
- Burst Balloons (hard DP, reverse order)
- Edit Distance (complex transitions)
- Russian Doll Envelopes (DP + binary search)
```

## How to Solve

### Step 1: Understand the Problem
```
□ Read problem 2-3 times
□ Understand input/output types
□ Identify constraints (array size, time limits)
□ Work through 2-3 examples manually
□ Find edge cases (empty, single, duplicates)
```

### Step 2: Plan Your Approach
```
□ Try brute force first (clarifies problem)
□ Recognize pattern (similar to which problem?)
□ Categorize (search, DP, graph, etc.)
□ Estimate time/space complexity needed
□ Identify optimizations
```

### Step 3: Code with Confidence
```
□ Use approach template from pattern
□ Write clean variable names
□ Add comments for tricky parts
□ Handle edge cases explicitly
□ Test with examples before submitting
```

### Step 4: Optimize & Verify
```
□ Find bottlenecks
□ Can we reduce loops?
□ Better data structure?
□ Verify time/space limits met
□ Check edge cases again
```

## Hint System

**Level 1: Tiny hint (reveals nothing)**
- Points toward right direction
- Example: "Consider using a hash set"

**Level 2: Medium hint (gives approach)**
- Explains algorithm pattern
- Example: "Use two pointers from opposite ends"

**Level 3: Big hint (pseudo-code)**
- Shows structure without solution
- Example: Algorithm outline with placeholders

## Solution Quality

Each solution includes:
1. **Explanation:** Why this approach works
2. **Complexity:** Time O(?), Space O(?)
3. **Code:** Clean, well-commented
4. **Variations:** Alternative approaches + trade-offs
5. **Interview tips:** What they're testing

## Problem Difficulty Guide

**Easy (5-10 min):**
- Straightforward implementation
- One approach clearly best
- Tests coding ability

**Medium (15-30 min):**
- Algorithm pattern not obvious
- Multiple valid approaches
- Tests problem-solving

**Hard (30-60 min):**
- Complex algorithm needed
- Tricky edge cases
- Tests advanced skills

## Performance Tracking

Your stats:
```
/problem stats

Total solved: 47/150
By category:
  - Arrays: 10/15 (67%)
  - Strings: 8/12 (67%)
  - Trees: 5/15 (33%)  ← Weak area
  - Graphs: 6/12 (50%)
  - DP: 18/30 (60%)

Pass rate: 62% (attempt count considered)
Weak areas: Trees (33%), Graphs (50%)
Recommended next: Tree problems to improve

Streak: 5 problems correct
Best: 8-problem streak
```

## Features Coming Soon

- **Code submission with auto-judge:** Write code, test against cases
- **Similar problems:** "You solved this, try similar"
- **Discussion:** Share approaches, learn from community
- **Video solutions:** Visual walkthrough of hard problems
- **Certificates:** Solve 50 in category → Certificate

## Interview Prep with /problem

**For Google/Facebook/Apple:**
1. Solve: Medium array + string problems (15)
2. Solve: Hard DP problems (10)
3. Solve: Graph algorithms (8)
4. Solve: Systems design (harder problems) (5)

**Total: ~60-80 problems for solid prep**

---

**Start solving:** `/problem arrays easy` for easiest array problems! 💪
