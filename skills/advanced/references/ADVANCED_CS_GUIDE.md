# Advanced Computer Science Guide

## Distributed Systems

### CAP Theorem
```
       Consistency
          /\
         /  \
        /    \
       /  CA  \  ← Single node only
      /________\
     /          \
    / CP      AP \
   /    Partition \
  /    Tolerance   \
 ──────────────────
Availability
```

**Choose two** (Partition tolerance usually required):
- **CP**: Strong consistency, may block during partition
- **AP**: Always available, eventual consistency

### Consensus (Raft)
```python
class RaftNode:
    def __init__(self):
        self.state = "follower"  # follower, candidate, leader
        self.term = 0
        self.voted_for = None
        self.log = []

    def request_vote(self, candidate_term, candidate_id):
        if candidate_term > self.term:
            self.term = candidate_term
            self.voted_for = candidate_id
            return True
        return False

    def append_entries(self, leader_term, entries):
        if leader_term >= self.term:
            self.log.extend(entries)
            return True
        return False
```

## Cryptography

### RSA Key Generation
```python
# Simplified RSA concept
def rsa_keygen(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 65537  # Common public exponent
    d = pow(e, -1, phi)  # Private key
    return (e, n), (d, n)  # public, private

def encrypt(m, public_key):
    e, n = public_key
    return pow(m, e, n)

def decrypt(c, private_key):
    d, n = private_key
    return pow(c, d, n)
```

### Hash Properties
- **Pre-image resistance**: Given h, hard to find m where H(m) = h
- **Second pre-image**: Given m₁, hard to find m₂ where H(m₁) = H(m₂)
- **Collision resistance**: Hard to find any m₁, m₂ where H(m₁) = H(m₂)

## Compilers

### Compilation Pipeline
```
Source Code
    ↓
┌─────────────┐
│  Lexer      │ → Tokens
└─────────────┘
    ↓
┌─────────────┐
│  Parser     │ → AST
└─────────────┘
    ↓
┌─────────────┐
│  Semantic   │ → Annotated AST
└─────────────┘
    ↓
┌─────────────┐
│  IR Gen     │ → Intermediate Representation
└─────────────┘
    ↓
┌─────────────┐
│  Optimizer  │ → Optimized IR
└─────────────┘
    ↓
┌─────────────┐
│  Code Gen   │ → Machine Code
└─────────────┘
```

## Quantum Computing

### Quantum Gates
```
Hadamard (H):
|0⟩ → (|0⟩ + |1⟩)/√2
|1⟩ → (|0⟩ - |1⟩)/√2

CNOT:
|00⟩ → |00⟩
|01⟩ → |01⟩
|10⟩ → |11⟩
|11⟩ → |10⟩
```

### Quantum Supremacy
- Shor's Algorithm: Factor N in O((log N)³)
- Grover's Algorithm: Search in O(√N)

---

*Computer Science Plugin - Advanced Skill*
