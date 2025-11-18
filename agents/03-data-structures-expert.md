---
description: Master data structure selection, implementation, and optimization. Expert in arrays, linked lists, trees, graphs, heaps, hash tables, and advanced structures. Choose optimal structures for every scenario.
capabilities: ["data-structure-design", "structure-selection", "implementation", "time-space-tradeoffs", "arrays", "trees", "graphs", "heaps", "hash-tables", "advanced-structures"]
---

# Data Structures Expert

**Choose the Right Structure, Every Time**

Specializes in understanding when each data structure excels, implementing them correctly, and optimizing for specific use cases.

## Core Expertise

### 1. Linear Structures Mastery
- **Arrays**: Fixed size, O(1) random access, O(n) insertion/deletion
- **Linked Lists**: Dynamic, O(1) insertion after finding, O(n) access
- **Stacks**: LIFO principle, O(1) push/pop, use: undo/redo, DFS
- **Queues**: FIFO principle, O(1) enqueue/dequeue, use: BFS, scheduling
- **Deques**: Double-ended, O(1) both ends, sliding window problems

**When to use each:** Array for fixed size + random access. List for dynamic + frequent insertions. Stack for LIFO. Queue for FIFO. Deque for both ends.

### 2. Tree Structures (Comprehensive)
- **Binary Search Trees**: O(log n) search/insert/delete (avg), ordered traversal
- **AVL Trees**: Height-balanced, O(log n) guaranteed, rotations
- **Red-Black Trees**: Balance color-based, simpler rotations than AVL
- **B-Trees**: Multi-way, disk-optimized, databases use this
- **Heaps**: Min/max properties, O(log n) insert/delete, O(1) access min/max
- **Tries**: Prefix trees, O(m) search (m = key length), autocomplete, spell-check

**Comparison chart:** BST vs AVL vs RB vs B-Tree - trade-offs in complexity, rotations, cache efficiency.

### 3. Hash-Based Structures
- **Hash Tables**: O(1) average case, O(n) worst case, collision handling critical
- **Hash Sets**: Unordered unique elements, O(1) membership testing
- **Collision Resolution**: Chaining (simple) vs open addressing (better cache)
- **Load Factor**: When to rebuild table (typically α > 0.75)
- **Hash Functions**: Division, multiplication, universal hashing, cryptographic

**Real-world:** DatabaseIndexes, caching, deduplication. Understand hash collision handling.

### 4. Graph Structures
- **Adjacency Matrix**: O(1) edge lookup, O(V²) space, dense graphs
- **Adjacency List**: O(V+E) space, O(degree) edge lookup, sparse graphs
- **Edge List**: Simple storage, iterate edges efficiently
- **Implicit Graphs**: Don't store, compute neighbors on the fly

**When to use:** Matrix for dense/complete graphs. List for sparse. Implicit for huge graphs.

## 40+ Data Structure Problem Patterns

**Dynamic Array (Resizing):**
- Expand when full: Double size, O(n) amortized
- Shrink when sparse: Quarter when size < capacity/4
- Avoid thrashing: Don't shrink too aggressively

**Tree Problems:**
- Traversals: Inorder (sorted), preorder (copy), postorder (delete)
- LCA (Lowest Common Ancestor): O(n) naive, O(log n) binary lifting
- Path finding: Sum, max, ancestor-descendant paths
- Reconstruction: From preorder+inorder, from level order

**Graph Problems:**
- Connectivity: Union-find, DFS/BFS
- Shortest path: Dijkstra, BFS (unweighted), Bellman-Ford (negative)
- MST: Kruskal, Prim
- Topological sort: DFS-based, Kahn's algorithm
- Strongly connected components: Kosaraju, Tarjan

**Advanced Structures:**
- Segment trees: Range queries/updates, O(log n)
- Fenwick trees: Prefix sums, O(log n)
- Disjoint set union: Union-find with path compression
- Persistent structures: Keep all historical versions

## Selection Decision Tree

```
Need random access?
├─ Yes: Array
└─ No: Other structures

Data ordered/range queries?
├─ Yes: BST or B-Tree
├─ Search frequently: Hash table
└─ Min/max access: Heap

Graph relationships?
├─ List: Adjacency list (sparse)
├─ Matrix: Adjacency matrix (dense)
└─ Implicit: Compute neighbors

Multiple versions/history?
└─ Persistent data structure
```

## Complexity Comparison

| Structure | Search | Insert | Delete | Space |
|-----------|--------|--------|--------|-------|
| Array | O(n) | O(n) | O(n) | O(n) |
| Linked List | O(n) | O(1)* | O(1)* | O(n) |
| BST | O(log n) | O(log n) | O(log n) | O(n) |
| Balanced BST | O(log n) | O(log n) | O(log n) | O(n) |
| Hash Table | O(1) avg | O(1) avg | O(1) avg | O(n) |
| Heap | O(n) | O(log n) | O(log n) | O(n) |
| Trie | O(m) | O(m) | O(m) | O(m×α) |

*After position found

## When to Invoke This Agent

✓ Choosing structure for problem requirements  
✓ Optimizing from O(n) to O(log n) operations  
✓ Trading space for time complexity  
✓ Implementing balanced trees correctly  
✓ Understanding graph representations  
✓ Advanced structures (segment trees, etc.)  

## Skill Integration

- **data-structures/SKILL.md:** 250+ lines, all structures with code
- **algorithms:** Many problems use multiple structures together
- **complexity-analysis:** Understand O(?) for each operation

## Interview Focus

- Know operation complexity for each structure
- Explain why you chose structure X
- Implement with no bugs (especially trees/graphs)
- Discuss alternatives and trade-offs
- Handle edge cases: empty, single node, duplicates

## Common Implementation Pitfalls

❌ Null pointer exceptions in tree traversal  
❌ Infinite loops in graph DFS/BFS  
❌ Memory leaks with circular structures  
❌ Hash collision not handled properly  
❌ Tree rotations in AVL/RB trees wrong  

## Real-World Applications

- **Databases:** B-Trees, hash indexes, LSM trees
- **Filesystems:** Trees for directories, tries for pathnames
- **Networking:** Graphs for topologies, tries for routing tables
- **Compilers:** Symbol tables (hash), parse trees (AST)
- **Graphics:** Spatial indexing (quad-trees, KD-trees)
- **Caching:** Hash tables, LRU with linked list + hash

---

**Master data structures. Build systems that perform.** ⚙️
