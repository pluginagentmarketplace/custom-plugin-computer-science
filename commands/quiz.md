---
name: quiz
description: /quiz
allowed-tools: Read
---

# /quiz

Test your Computer Science knowledge with adaptive, comprehensive quizzes across all domains.

## Quick Usage

```
/quiz [domain]              → Take quiz in domain
/quiz [domain] [difficulty] → Specific difficulty (easy/medium/hard)
/quiz all comprehensive     → Full assessment all domains
/quiz [domain] timed        → 60-second round
/quiz stats                 → Your quiz history and scores
/quiz resume                → Continue interrupted quiz
```

## Quiz Domains

### 1. Foundations Quiz (20 questions)
**Topics:** Logic, proofs, set theory, combinatorics, number theory

**Sample questions:**
- Explain mathematical induction with example (Medium)
- Prove by contradiction: √3 is irrational (Medium)
- How many ways to arrange 5 distinct objects? (Easy)
- What's the Pigeonhole Principle? (Easy)
- Solve: x ≡ 3 (mod 5) and x ≡ 2 (mod 7) (Hard)

**Passing:** 16/20 (80%)

### 2. Algorithms Quiz (25 questions)
**Topics:** Sorting, searching, DP, greedy, backtracking

**Sample:**
- Compare merge sort vs quick sort (Easy)
- When is greedy algorithm optimal? Explain. (Medium)
- Solve coin change problem for n=10 (Hard)
- Design DP solution for knapsack (Hard)

**Passing:** 20/25 (80%)

### 3. Data Structures Quiz (20 questions)
**Topics:** Linear, trees, graphs, hashes, advanced

**Sample:**
- BST search complexity? Why? (Easy)
- When use linked list vs array? (Medium)
- Implement LRU cache using hash + list (Hard)

**Passing:** 16/20 (80%)

### 4. Complexity Theory Quiz (15 questions)
**Topics:** Big O, Master Theorem, NP-completeness, computability

**Sample:**
- What's Big O vs Big Theta? (Easy)
- Apply Master Theorem: T(n)=3T(n/2)+n (Medium)
- Reduce 3-SAT to prove NP-completeness (Hard)

**Passing:** 12/15 (80%)

### 5. Systems Quiz (20 questions)
**Topics:** CPU, memory, OS, networks, databases, distributed

**Sample:**
- Explain CPU cache hierarchy (Easy)
- Virtual memory: paging vs segmentation? (Medium)
- Design replicated database with CAP theorem (Hard)

**Passing:** 16/20 (80%)

## Question Types

### Multiple Choice
4 options, select best answer

### True/False
Statement evaluation

### Short Answer (2-3 minutes)
Write explanation or short code

### Code Completion
Finish the function

### Problem Solving
Design or optimize algorithm

### Matching
Connect concepts to definitions

## Difficulty Levels

**Easy (5 min):** Basic recall, straightforward application
**Medium (10 min):** Requires understanding and analysis
**Hard (15 min):** Deep knowledge, synthesis, tricky edge cases

## How Scoring Works

**Correct answer:**
- Easy: +10 points
- Medium: +15 points
- Hard: +25 points

**Streak bonus:** 3+ correct → +5 bonus
**Speed bonus:** Answer in <2 min → +5 bonus
**Total possible:** 500 points per full quiz

## Quiz Modes

### Practice Mode
- Instant feedback on every question
- Explanations provided
- No time limit
- Repeat unlimited

### Timed Mode
- 60 seconds per question
- Speed bonus available
- No feedback until end
- Simulates interview

### Adaptive Mode
- Questions adjust to your level
- Start easy, increase difficulty
- Focuses on weak areas
- Personalized assessment

### Competitive Mode
- Leaderboards
- Weekly challenges
- Badges and achievements
- Community rankings

## Performance Tracking

```
/quiz stats

Overall Score: 342/500 (68%)

By domain:
  Foundations: 16/20 (80%) ✓ Mastery
  Algorithms: 18/25 (72%) ~ Competent
  Data Structures: 14/20 (70%) ~ Competent
  Complexity: 10/15 (67%) ~ Learning
  Systems: 12/20 (60%) ~ Needs work ← Focus here

Weak topics:
  1. NP-completeness (50%)
  2. Memory management (55%)
  3. Distributed systems (60%)

Recommended action:
  1. Review complexity theory fundamentals
  2. Take systems quiz again (medium difficulty)
  3. Study distributed consensus (CAP theorem)

Streaks:
  Current: 3 correct
  Best: 8 correct
  Days active: 12/30
```

## Quiz Badges

🥉 **Bronze:** Score 50%+ on any domain  
🥈 **Silver:** Score 80%+ on any domain  
🥇 **Gold:** Score 90%+ on any domain  
💎 **Platinum:** Score 95%+ on all domains  
🌟 **Streak Master:** 10+ consecutive correct  
⚡ **Speed Demon:** Answer 5 hard in <5min  
🎓 **CS Scholar:** Master all domains (90%+)  

## Interview Simulation

**Simulate actual interview:**
```
/quiz interview-prep

Conditions:
- 3 problems in 90 minutes
- Time tracking
- No explanations until end
- Difficulty: Medium-Hard
- Mix of domains

Topics selected:
1. DP Algorithm (15 min)
2. System Design (30 min)
3. Complexity Analysis (10 min)

Result: Score + feedback
```

## Tips for Success

**Before quiz:**
- Review related material
- Have paper/whiteboard ready
- Quiet, distraction-free space

**During quiz:**
- Read question carefully
- Think before answering
- Flag difficult questions
- Review if time permits

**After quiz:**
- Review all explanations
- Understand wrong answers
- Identify weak areas
- Schedule remedial study

## Continuous Learning

**Recommended flow:**
1. Take Foundations quiz → 70% pass? → Study more
2. Study foundations 1 week
3. Take quiz again → 80% pass? → Move on
4. Repeat for each domain
5. Full assessment after all
6. Focused revision on weak areas
7. Final mastery assessment

**Typical timeline:**
- Foundations: 1 week
- Algorithms: 2-3 weeks
- Data Structures: 1-2 weeks
- Complexity: 1-2 weeks
- Systems: 1-2 weeks
- **Total: 6-10 weeks to mastery**

---

**Assess your knowledge:** `/quiz foundations easy` to start! 📝
