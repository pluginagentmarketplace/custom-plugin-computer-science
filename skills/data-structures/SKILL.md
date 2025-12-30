---
name: data-structures
description: Master selection and implementation of data structures. Learn when to use arrays, lists, trees, graphs, heaps, and hash tables for optimal performance.
sasmp_version: "1.3.0"
bonded_agent: 03-data-structures-expert
bond_type: PRIMARY_BOND
---

# Data Structures Skill

## Skill Metadata

```yaml
skill_config:
  version: "1.0.0"
  category: implementation
  prerequisites: [cs-foundations]
  estimated_time: "6-8 weeks"
  difficulty: intermediate

  parameter_validation:
    structure_type:
      type: string
      enum: [array, list, tree, heap, hash, graph, trie]
      required: true
    operation:
      type: string
      enum: [search, insert, delete, traverse]

  retry_config:
    max_attempts: 3
    backoff_strategy: exponential
    initial_delay_ms: 500

  observability:
    log_level: INFO
    metrics: [structure_usage, operation_complexity]
```

---

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

**Balanced Trees**
- AVL: height-balanced
- Red-Black: color-based balancing
- B-Trees: multi-way
- Guarantee O(log n) operations

**Heaps**
- Min/Max heap property
- Insert/delete O(log n), Build O(n)
- Use: Priority queues, heap sort

### Hash Structures

**Hash Tables**
- Average O(1) operations
- Collision handling: chaining, open addressing
- Load factor matters

---

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

---

## Complexity Comparison

| Operation | Array | List | BST | Hash | Heap |
|-----------|-------|------|-----|------|------|
| Search | O(n) | O(n) | O(log n) | O(1) avg | O(n) |
| Insert | O(n) | O(1)* | O(log n) | O(1) avg | O(log n) |
| Delete | O(n) | O(1)* | O(log n) | O(1) avg | O(log n) |

---

## Troubleshooting

| Issue | Root Cause | Resolution |
|-------|------------|------------|
| Hash collision storm | Poor hash function | Improve hash, use chaining |
| Tree degenerates | Sorted insertions | Use balanced tree (AVL/RB) |
| Memory exhaustion | No size limits | Add capacity limits |
| Iterator invalidation | Modify during iteration | Use safe iteration pattern |

---

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
