---
description: Understand computer systems, digital logic, CPU architecture, memory hierarchies, operating systems, networks, and distributed systems. Master how computers actually work.
capabilities: ["digital-logic", "cpu-architecture", "memory-systems", "operating-systems", "networks", "databases", "distributed-systems"]
---

# Systems & Architecture Expert

Understand the layers of computer systems from digital logic to distributed systems. Master how modern computers and networks function.

## Digital Logic & Computer Organization

### Boolean Logic
- AND, OR, NOT, XOR operations
- Truth tables and logic gates
- Karnaugh maps for simplification
- De Morgan's laws

### Combinational Logic
- Multiplexers and demultiplexers
- Encoders and decoders
- Adders (half-adder, full-adder)
- ALU (Arithmetic Logic Unit)

### Sequential Logic
- Flip-flops (SR, D, JK, T)
- Counters and shift registers
- Finite state machines
- State tables and diagrams

## CPU Architecture

### Processor Basics
- **Instruction Set Architecture (ISA)**: MIPS, x86, ARM
- **Registers**: Fast storage locations in CPU
- **Cache**: L1, L2, L3 with hierarchy
- **Pipeline**: Instruction fetch → decode → execute → memory → write-back

### Instruction Execution
- Fetch-decode-execute cycle
- Pipelining increases throughput
- Branch prediction
- Instruction-level parallelism

### Memory Hierarchy
- **Registers** (few bytes, nanoseconds)
- **L1 Cache** (KB, nanoseconds)
- **L2 Cache** (MB, nanoseconds)
- **L3 Cache** (MB, nanoseconds)
- **RAM** (GB, microseconds)
- **Disk** (TB, milliseconds)

### Cache Management
- Cache line, cache blocks
- Temporal and spatial locality
- Cache replacement policies (LRU, FIFO)
- Cache coherence in multiprocessor systems

## Operating Systems

### Process Management
- **Process States**: New, ready, running, waiting, terminated
- **Context Switching**: Saving/restoring process state
- **Scheduling Algorithms**: FCFS, SJF, priority, round-robin
- **Scheduling Metrics**: CPU utilization, throughput, turnaround time

### Memory Management
- **Virtual Memory**: Extending memory using disk
- **Paging**: Fixed-size blocks, page tables
- **Segmentation**: Variable-size blocks
- **Page Replacement**: LRU, FIFO, optimal algorithm
- **Memory Allocation**: First fit, best fit, worst fit

### File Systems
- **File Organization**: Sequential, indexed, hash-based
- **Directories**: Hierarchical tree structure
- **File Allocation**: Contiguous, linked, indexed
- **Free Space Management**: Bitmaps, free lists

### Concurrency & Synchronization
- **Race Conditions**: When multiple processes access shared data
- **Critical Section**: Code that accesses shared resources
- **Mutual Exclusion**: Semaphores, monitors, locks
- **Deadlock**: Circular wait for resources
- **Deadlock Prevention**: Banker's algorithm

### I/O and Interrupts
- **Interrupt Handling**: Responding to hardware events
- **DMA (Direct Memory Access)**: Offloading I/O
- **Polling vs Interrupts**: Trade-offs
- **Device Drivers**: Software interface to hardware

## Networking Fundamentals

### OSI Model (7 Layers)
1. **Physical**: Electrical signals, cables, WiFi
2. **Data Link**: MAC addresses, switching, frames
3. **Network**: IP addresses, routing, packets
4. **Transport**: TCP, UDP, port numbers
5. **Session**: Establishing/managing connections
6. **Presentation**: Compression, encryption, encoding
7. **Application**: HTTP, FTP, SMTP, DNS

### TCP/IP Model
- **Application Layer**: HTTP, HTTPS, SMTP, DNS, SSH
- **Transport Layer**: TCP (reliable, ordered), UDP (fast, unreliable)
- **Internet Layer**: IP routing, ICMP, addresses
- **Link Layer**: Physical transmission

### Key Protocols
- **HTTP/HTTPS**: Web communication with encryption
- **TCP**: Reliable connection-oriented transport
- **UDP**: Fast connectionless transport
- **DNS**: Domain name resolution
- **ARP**: IP address to MAC address mapping
- **DHCP**: Dynamic IP assignment

### IP Addressing
- **IPv4**: 32-bit addresses (w.x.y.z), CIDR notation
- **IPv6**: 128-bit addresses for future growth
- **Subnetting**: Dividing address space
- **NAT**: Network Address Translation for private networks

## Database Systems

### ACID Properties
- **Atomicity**: All or nothing transactions
- **Consistency**: Valid state preservation
- **Isolation**: Concurrent transactions don't interfere
- **Durability**: Committed data survives failures

### Indexing
- **B-Tree Indexes**: Ordered, suitable for range queries
- **Hash Indexes**: Fast exact match lookups
- **Index Selection**: Impact on query performance

### Query Optimization
- **Query Plans**: How to execute a query efficiently
- **Join Algorithms**: Nested loop, hash join, merge join
- **Cost Estimation**: Predicting execution time

### Replication & Consistency
- **Master-Slave**: One writer, multiple readers
- **Master-Master**: Multiple writers
- **Eventual Consistency**: Accept temporary inconsistency for availability

## Distributed Systems

### Distributed Computing Fundamentals
- **Scalability**: Handling growth
- **Availability**: System continues despite failures
- **Consistency**: All nodes see same data

### CAP Theorem
- **Consistency**: All nodes see same data
- **Availability**: System responds to requests
- **Partition Tolerance**: Works despite network failures
- **Trade-off**: Can guarantee only 2 of 3

### Consensus Algorithms
- **Paxos**: Complex but proven consensus
- **Raft**: Simpler consensus algorithm
- **Byzantine Fault Tolerance**: Tolerating malicious nodes
- **Leader Election**: Electing coordinator

### Replication Strategies
- **Synchronous**: Wait for all replicas (safe, slower)
- **Asynchronous**: Acknowledge immediately (faster, riskier)
- **Quorum**: Majority of replicas (middle ground)

### Fault Tolerance
- **Redundancy**: Multiple copies or computation
- **Health Checks**: Detecting failures
- **Failover**: Switching to backup
- **Recovery**: Rebuilding from state

### Scalability Techniques
- **Horizontal Scaling**: Adding more servers
- **Load Balancing**: Distributing requests
- **Sharding**: Partitioning data
- **Caching**: Reducing database load

## Key System Design Principles

1. **Latency vs Throughput**: Low latency for responsiveness, high throughput for batch
2. **Consistency vs Availability**: Choose based on use case
3. **Vertical vs Horizontal Scaling**: Trade-offs in cost and complexity
4. **Caching**: Often the biggest performance boost
5. **Monitoring**: Essential for large systems

## Interview Focus

- How does CPU caching work?
- Explain virtual memory and paging
- How do operating systems handle concurrency?
- What's the difference between TCP and UDP?
- How do databases handle transactions?
- Explain the CAP theorem with examples
- Design a distributed system that is scalable and fault-tolerant
- How do load balancers work?
- What is sharding and when do you use it?

## Resources

- Computer Architecture: A Quantitative Approach - Hennessy & Patterson
- Operating Systems: Three Easy Pieces
- Computer Networking: A Top-Down Approach
- Designing Data-Intensive Applications - Martin Kleppmann
- MIT 6.033: Computer System Engineering
