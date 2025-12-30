---
name: learn
description: Start guided CS learning paths from foundations to advanced topics
allowed-tools: Read
sasmp_version: "1.3.0"
---

# /learn

Start your Computer Science learning journey with expertly designed paths.

## Command Schema

```yaml
command_config:
  version: "1.0.0"

  input_validation:
    path:
      type: string
      enum: [foundations, algorithms, data-structures, systems, full-path]
      required: false
    action:
      type: string
      enum: [status, resume, restart, switch, stats]
      required: false

  exit_codes:
    0: success
    1: invalid_path
    2: path_not_started
    3: assessment_failed
```

## Quick Usage

```
/learn foundations      # 4-week foundation building
/learn algorithms       # 8-week algorithms mastery
/learn data-structures  # 6-week structures mastery
/learn systems          # 10-week systems deep dive
/learn full-path        # 24-week complete CS education
/learn status           # Check your learning progress
/learn resume           # Resume previous learning path
```

---

## Learning Paths

### Path 1: Foundations (4 weeks)

**Goal:** Build unshakeable CS fundamentals

| Week | Topics | Problems |
|------|--------|----------|
| 1 | Logic & Proofs | 5 |
| 2 | Set Theory & Relations | 8 |
| 3 | Combinatorics | 10 |
| 4 | Number Theory & Graphs | 10 |

**Assessment:** 80%+ quiz score to continue

### Path 2: Algorithms (8 weeks)

**Prerequisite:** Comfortable with loops and recursion

| Weeks | Topics | Problems |
|-------|--------|----------|
| 1-2 | Searching & Sorting | 15 |
| 3-4 | D&C + DP Part 1 | 20 |
| 5-6 | DP Part 2 + Greedy | 30 |
| 7-8 | Backtracking + Interview | 35 |

**Assessment:** Solve 3 problems in 90 minutes

### Path 3: Data Structures (6 weeks)

| Weeks | Topics | Problems |
|-------|--------|----------|
| 1-2 | Linear Structures | 20 |
| 3-4 | Trees | 25 |
| 5-6 | Advanced + Graphs | 25 |

### Path 4: Systems (10 weeks)

**Prerequisite:** Complete 2+ previous paths

Covers: CPU, memory, OS, networks, databases, distributed systems.

### Path 5: Full Stack (24 weeks)

Sequential combination of all paths with integrated projects.

---

## Progress Commands

```
/learn status     # Current progress, next milestone
/learn resume     # Continue from where you left off
/learn restart    # Reset and start fresh
/learn switch     # Change to different path
/learn stats      # Detailed progress statistics
```

---

## Learning Features

- **Progress Tracking:** Problems solved, pass rate, weak areas
- **Hint System:** 3-level hints (avoid spoilers)
- **Solution Judge:** Auto-test your code
- **Weekly Reports:** Summary of progress

---

## Tips for Success

- **30-60 mins daily** > 5 hours weekend
- **Use hints** when stuck 30+ mins
- **Review** explanations even for correct answers
- **Spaced repetition** for long-term retention

---

## Path Summary

| Path | Topics | Problems | Hours | Prerequisites |
|------|--------|----------|-------|---------------|
| Foundations | Logic, Sets, Combinatorics | 30+ | 25-30 | None |
| Algorithms | Sorting, DP, Greedy | 100+ | 40-50 | Foundations |
| Data Structures | Arrays, Trees, Graphs | 50+ | 30-40 | Algorithms |
| Systems | CPU, OS, Networks | 40+ | 45-55 | Alg + DS |
| Full Stack | All integrated | 250+ | 140-180 | Commitment |

---

**Start:** `/learn foundations` for beginners, `/learn algorithms` for interview prep.
