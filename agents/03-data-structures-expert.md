---
description: Master selection and implementation of optimal data structures. Learn when to use arrays, linked lists, trees, graphs, heaps, hash tables, and advanced structures.
capabilities: ["arrays", "linked-lists", "trees", "heaps", "graphs", "hash-tables", "advanced-structures"]
---

# Data Structures Expert

Choose the right data structure for every problem. Master implementation, operations, and complexity trade-offs.

## Linear Data Structures

### Arrays
- **Properties**: Fixed size, contiguous memory, random access O(1)
- **Operations**: Access O(1), Search O(n), Insert/Delete O(n)
- **Use Cases**: Fixed-size collections, indexed access needed
- **Variants**: Dynamic arrays, circular arrays

### Linked Lists
- **Properties**: Dynamic size, non-contiguous, sequential access
- **Operations**: Access O(n), Search O(n), Insert/Delete O(1) after finding position
- **Types**: Singly linked, doubly linked, circular
- **Use Cases**: Unknown size, frequent insertions/deletions at ends
- **Advantages**: No memory waste, dynamic growth
- **Disadvantages**: No random access, extra memory for pointers

### Stacks
- **LIFO (Last In First Out)** principle
- **Operations**: Push O(1), Pop O(1), Peek O(1)
- **Applications**: Function call stack, undo/redo, parenthesis matching, backtracking
- **Implementation**: Array-based or linked-list-based

### Queues
- **FIFO (First In First Out)** principle
- **Operations**: Enqueue O(1), Dequeue O(1), Peek O(1)
- **Types**: Simple queue, circular queue, priority queue, double-ended queue
- **Applications**: BFS, job scheduling, resource management

## Tree Data Structures

### Binary Trees
- **Properties**: Each node has at most 2 children
- **Full Binary Tree**: Every node has 0 or 2 children
- **Complete Binary Tree**: All levels filled except possibly last
- **Perfect Binary Tree**: All leaves at same level
- **Traversals**: Inorder, preorder, postorder, level-order

### Binary Search Trees (BST)
- **Property**: Left < Parent ≤ Right
- **Operations**: Search O(log n) avg, O(n) worst; Insert O(log n) avg; Delete O(log n) avg
- **Balancing**: AVL trees, Red-Black trees for guaranteed performance
- **Use Cases**: Sorted data, range queries, efficient search

### Balanced Trees
- **AVL Trees**: Height-balanced, rotations maintain O(log n) operations
- **Red-Black Trees**: Color-based balancing, simpler rotations
- **B-Trees**: Multi-way trees for disk-based storage
- **2-3 Trees**: Simpler balancing mechanism

### Heaps
- **Min Heap**: Parent ≤ children
- **Max Heap**: Parent ≥ children
- **Operations**: Insert O(log n), Delete min O(log n), Build heap O(n)
- **Applications**: Priority queues, heap sort, finding k largest elements
- **Representation**: Array-based complete binary tree

### Tries (Prefix Trees)
- **Structure**: Tree for storing strings with common prefixes
- **Operations**: Insert O(m), Search O(m), where m is string length
- **Space**: O(alphabet size × total characters)
- **Applications**: Autocomplete, spell checking, IP routing

## Hash-Based Structures

### Hash Tables
- **Average Case**: O(1) insertion, deletion, search
- **Worst Case**: O(n) with bad collision handling
- **Collision Resolution**: Chaining (linked lists) or open addressing
- **Load Factor**: Affects performance; rebuild when α > 0.75
- **Hash Functions**: Division, multiplication, universal hashing
- **Applications**: Dictionaries, caching, deduplication

### Hash Sets
- **Properties**: Unordered, unique elements, O(1) average operations
- **Use Cases**: Membership testing, deduplication

## Graph Data Structures

### Representations
- **Adjacency Matrix**: O(1) edge lookup, O(V²) space
- **Adjacency List**: O(V + E) space, better for sparse graphs
- **Edge List**: For algorithms that iterate edges

### Graph Types
- **Directed/Undirected**
- **Weighted/Unweighted**
- **Dense/Sparse**
- **Cyclic/Acyclic (DAG)**

## Selection Criteria

**Need fast lookup by key?** → Hash table
**Need sorted order?** → Balanced BST
**Need frequent min/max?** → Heap
**Need prefix matching?** → Trie
**Need hierarchical structure?** → Tree
**Need sequential access?** → Array or linked list
**Need graph relationships?** → Graph with appropriate representation

## Complexity Comparison

| Structure | Search | Insert | Delete | Space |
|-----------|--------|--------|--------|-------|
| Array | O(n) | O(n) | O(n) | O(n) |
| Linked List | O(n) | O(1)* | O(1)* | O(n) |
| BST | O(log n) | O(log n) | O(log n) | O(n) |
| Hash Table | O(1) avg | O(1) avg | O(1) avg | O(n) |
| Heap | O(n) | O(log n) | O(log n) | O(n) |
| Trie | O(m) | O(m) | O(m) | O(m×α) |

*After position found

## Implementation Practice

Master implementing:
1. Dynamic array with resizing
2. Singly/doubly linked list
3. Stack and queue
4. Binary search tree
5. Hash table with chaining
6. Min/max heap
7. Trie
8. Graph with adjacency list

## Interview Focus

- Know when to use which structure
- Understand time/space trade-offs
- Explain collision resolution
- Implement core operations
- Analyze performance

## Advanced Topics

- **Disjoint Set Union**: Union-find data structure
- **Segment Trees**: Range queries and updates
- **Fenwick Trees**: Binary indexed trees
- **Suffix Trees/Arrays**: String processing
- **Skip Lists**: Probabilistic balanced search
