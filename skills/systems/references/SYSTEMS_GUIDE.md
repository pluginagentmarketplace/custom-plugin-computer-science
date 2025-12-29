# Computer Systems Guide

## Operating Systems

### Process Scheduling
```python
# Round Robin Simulation
def round_robin(processes, quantum):
    queue = list(processes)
    time = 0
    while queue:
        process = queue.pop(0)
        run_time = min(quantum, process['remaining'])
        process['remaining'] -= run_time
        time += run_time
        if process['remaining'] > 0:
            queue.append(process)
        else:
            process['completion'] = time
    return processes
```

### Deadlock Conditions (All 4 required)
1. **Mutual Exclusion** - Resource held exclusively
2. **Hold and Wait** - Holding while waiting
3. **No Preemption** - Cannot force release
4. **Circular Wait** - Circular dependency chain

### Virtual Memory
```
Virtual Address → Page Table → Physical Address

┌─────────┬──────────┐    ┌─────────┬────────┐
│ Page #  │  Offset  │ →  │ Frame # │ Offset │
└─────────┴──────────┘    └─────────┴────────┘
```

## Networking

### TCP Three-Way Handshake
```
Client              Server
  │                   │
  │──── SYN ─────────→│
  │                   │
  │←─── SYN-ACK ──────│
  │                   │
  │──── ACK ─────────→│
  │                   │
  │   Connection      │
  │   Established     │
```

### HTTP Status Codes
| Code | Category |
|------|----------|
| 1xx | Informational |
| 2xx | Success |
| 3xx | Redirection |
| 4xx | Client Error |
| 5xx | Server Error |

## Databases

### ACID Properties
```python
# Transaction Example
try:
    db.begin_transaction()
    db.execute("UPDATE accounts SET balance = balance - 100 WHERE id = 1")
    db.execute("UPDATE accounts SET balance = balance + 100 WHERE id = 2")
    db.commit()  # Atomic, Consistent, Isolated, Durable
except:
    db.rollback()
```

### Indexing
```sql
-- B-Tree index for range queries
CREATE INDEX idx_date ON orders(order_date);

-- Hash index for equality
CREATE INDEX idx_id ON users USING HASH(id);
```

## Computer Architecture

### Pipeline Hazards
- **Structural**: Resource conflict
- **Data**: RAW, WAR, WAW dependencies
- **Control**: Branch prediction

### Cache Hierarchy
```
CPU Core
   ↓ (1-2 cycles)
L1 Cache (32-64 KB)
   ↓ (10 cycles)
L2 Cache (256 KB - 1 MB)
   ↓ (40 cycles)
L3 Cache (8-32 MB)
   ↓ (100+ cycles)
Main Memory (GB)
```

---

*Computer Science Plugin - Systems Skill*
