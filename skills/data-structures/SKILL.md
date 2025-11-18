---
name: data-structures
description: Master selection and implementation of data structures. Learn when to use arrays, lists, trees, graphs, heaps, and hash tables for optimal performance.
---

# Data Structures

## Quick Start

Choose the right structure for every problem. Master operations and trade-offs.

### Linear Structures

**Arrays**
- Random access O(1)
- Fixed size
- Cache friendly
- Use: Known size, frequent access

**Linked Lists**
- Dynamic size
- Sequential access O(n)
- Efficient insertion/deletion O(1)
- Types: Singly, doubly, circular

**Stacks**
- LIFO principle
- Push/pop O(1)
- Use: Undo/redo, parenthesis matching, DFS

**Queues**
- FIFO principle
- Enqueue/dequeue O(1)
- Types: Simple, circular, priority, deque
- Use: BFS, job scheduling

### Trees

**Binary Search Trees**
- Ordered storage
- Search/insert/delete O(log n) avg
- Traversals: inorder, preorder, postorder
- Use: Sorted data, range queries

**Balanced Trees**
- AVL: height-balanced
- Red-Black: color-based balancing
- B-Trees: multi-way
- Guarantee O(log n) operations

**Heaps**
- Min/Max heap property
- Insert/delete O(log n)
- Build O(n)
- Use: Priority queues, heap sort

**Tries**
- String prefix tree
- Insert/search O(m)
- Use: Autocomplete, spell check

### Hash Structures

**Hash Tables**
- Average O(1) operations
- Collision handling: chaining, open addressing
- Load factor matters
- Use: Dictionary, caching, deduplication

**Hash Sets**
- Unordered, unique elements
- O(1) membership testing
- Use: Deduplication, unique elements

### Graphs

**Representations**
- Adjacency matrix: O(1) edge lookup, O(V²) space
- Adjacency list: O(V+E) space
- Edge list: Iterate edges

**Graph Types**
- Directed/undirected
- Weighted/unweighted
- Dense/sparse

## Decision Matrix

| Need | Best Structure |
|------|----------------|
| Random access | Array |
| Frequent insertions/deletions | Linked list |
| Min/max element | Heap |
| Ordered traversal | BST |
| Fast lookup | Hash table |
| Prefix matching | Trie |
| Relations | Graph |
| Hierarchical | Tree |

## Complexity Comparison

| Operation | Array | List | BST | Hash | Heap |
|-----------|-------|------|-----|------|------|
| Search | O(n) | O(n) | O(log n) | O(1) avg | O(n) |
| Insert | O(n) | O(1)* | O(log n) | O(1) avg | O(log n) |
| Delete | O(n) | O(1)* | O(log n) | O(1) avg | O(log n) |

## Implementation Checklist

- [ ] Dynamic array with resizing
- [ ] Singly/doubly linked list
- [ ] Stack and queue
- [ ] Binary search tree
- [ ] AVL tree or Red-Black tree
- [ ] Hash table
- [ ] Min/max heap
- [ ] Trie
- [ ] Graph (adjacency list)
- [ ] Disjoint set union

## Advanced Topics

- Segment trees for range queries
- Fenwick trees for prefix sums
- Suffix trees for string matching
- Skip lists for probabilistic balance
- Bloom filters for membership
- Consistent hashing for caching

## Interview Focus

- Know operation complexities
- Understand space trade-offs
- Explain when to use which
- Implement core operations
- Analyze alternatives
