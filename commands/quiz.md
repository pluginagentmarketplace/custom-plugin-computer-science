---
name: quiz
description: Test CS knowledge with adaptive quizzes across all domains
allowed-tools: Read
sasmp_version: "1.3.0"
---

# /quiz

Test your Computer Science knowledge with adaptive, comprehensive quizzes.

## Command Schema

```yaml
command_config:
  version: "1.0.0"

  input_validation:
    domain:
      type: string
      enum: [foundations, algorithms, data-structures, complexity, systems, all]
      required: false
    difficulty:
      type: string
      enum: [easy, medium, hard]
      required: false
    mode:
      type: string
      enum: [practice, timed, adaptive, interview]
      default: practice

  exit_codes:
    0: success
    1: invalid_domain
    2: quiz_interrupted
    3: assessment_failed
```

## Quick Usage

```
/quiz foundations          # Take foundations quiz
/quiz algorithms medium    # Medium difficulty algorithms
/quiz all                  # Comprehensive assessment
/quiz timed                # 60-second per question
/quiz stats                # Your quiz history
/quiz resume               # Continue interrupted quiz
```

---

## Quiz Domains

| Domain | Questions | Passing | Topics |
|--------|-----------|---------|--------|
| Foundations | 20 | 80% | Logic, proofs, sets, combinatorics |
| Algorithms | 25 | 80% | Sorting, DP, greedy, backtracking |
| Data Structures | 20 | 80% | Trees, graphs, hashes |
| Complexity | 15 | 80% | Big O, Master Theorem, NP |
| Systems | 20 | 80% | CPU, OS, networks, distributed |

---

## Question Types

| Type | Format | Time |
|------|--------|------|
| Multiple Choice | 4 options | 1 min |
| True/False | Statement | 30 sec |
| Short Answer | Explanation | 2-3 min |
| Code Completion | Fill blanks | 3-5 min |
| Problem Solving | Design/optimize | 5-10 min |

---

## Difficulty Levels

| Level | Time | Description |
|-------|------|-------------|
| Easy | 5 min | Basic recall |
| Medium | 10 min | Analysis required |
| Hard | 15 min | Deep knowledge |

---

## Scoring System

| Correct Answer | Points |
|----------------|--------|
| Easy | +10 |
| Medium | +15 |
| Hard | +25 |
| Streak bonus (3+) | +5 |
| Speed bonus (<2min) | +5 |

---

## Quiz Modes

### Practice Mode
- Instant feedback
- Explanations provided
- No time limit
- Unlimited repeats

### Timed Mode
- 60 seconds per question
- Speed bonus available
- Simulates interview pressure

### Adaptive Mode
- Adjusts to your level
- Focuses on weak areas
- Personalized assessment

### Interview Mode
- 3 problems in 90 minutes
- Mixed difficulty
- Real interview conditions

---

## Performance Tracking

```
/quiz stats

Overall: 342/500 (68%)

By domain:
  Foundations: 80% ✓
  Algorithms: 72% ~
  Data Structures: 70% ~
  Complexity: 67% ~
  Systems: 60% ← Focus here

Weak topics:
  1. NP-completeness (50%)
  2. Memory management (55%)
  3. Distributed systems (60%)
```

---

## Badges

| Badge | Requirement |
|-------|-------------|
| Bronze | 50%+ any domain |
| Silver | 80%+ any domain |
| Gold | 90%+ any domain |
| Platinum | 95%+ all domains |
| Streak Master | 10+ consecutive |
| CS Scholar | Master all (90%+) |

---

## Tips for Success

**Before:** Review material, quiet space, paper ready

**During:** Read carefully, think before answering

**After:** Review explanations, identify weak areas

---

## Recommended Flow

1. Foundations quiz → 80%+ → Continue
2. Algorithms quiz → 80%+ → Continue
3. Data Structures → 80%+ → Continue
4. Complexity → 80%+ → Continue
5. Systems → 80%+ → Complete!

**Timeline:** 6-10 weeks to full mastery

---

**Start:** `/quiz foundations easy` to begin assessment.
