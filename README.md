# Developer Roadmap Learning Plugin

A comprehensive Claude Code plugin that brings the 65+ developer roadmaps from [kamranahmedse/developer-roadmap](https://github.com/kamranahmedse/developer-roadmap) into Claude Code with AI-powered learning guidance.

## 🚀 Features

### 7 Specialized Agents
1. **Frontend Development Specialist** - Web development, frameworks, UI/UX
2. **Backend Development Specialist** - Server-side, databases, APIs
3. **DevOps & Cloud Specialist** - Infrastructure, containerization, deployment
4. **Data Science & AI Specialist** - ML, data analysis, AI systems
5. **Languages & Fundamentals Specialist** - Programming languages, CS fundamentals
6. **Architecture & Design Specialist** - System design, patterns, scalability
7. **Security & Compliance Specialist** - Cybersecurity, secure coding, compliance

### 4 Powerful Commands
- **`/roadmap`** - Browse 65+ developer roadmaps by category
- **`/learning-path`** - Get personalized learning paths for any role
- **`/skills`** - View required skills and learning resources
- **`/assess`** - Self-assess knowledge across 7 domains

### 7 Skill Categories
- Frontend Development
- Backend Development
- DevOps & Infrastructure
- Data Science & AI
- Programming Languages & Fundamentals
- Architecture & System Design
- Security & Compliance

## 📦 Installation

### Quick Start
```bash
# Claude Code will auto-detect and load the plugin from this directory
```

## 🎯 Quick Start

### 1. Explore Roadmaps
```
/roadmap frontend
Shows all frontend development roadmaps with learning paths
```

### 2. Get Personalized Learning Path
```
/learning-path backend python
Creates 4-6 month plan to become a Python backend developer
```

### 3. View Required Skills
```
/skills devops kubernetes
Shows all DevOps and Kubernetes skills with resources
```

### 4. Self-Assess Knowledge
```
/assess all
Comprehensive assessment across all 7 domains
```

## 🏗️ Plugin Structure

```
.
├── .claude-plugin/
│   └── plugin.json                    # Plugin manifest
├── agents/                            # 7 AI specialists
│   ├── 01-frontend-specialist.md
│   ├── 02-backend-specialist.md
│   ├── 03-devops-specialist.md
│   ├── 04-data-ai-specialist.md
│   ├── 05-languages-specialist.md
│   ├── 06-architecture-specialist.md
│   └── 07-security-specialist.md
├── commands/                          # Slash commands
│   ├── roadmap.md
│   ├── learning-path.md
│   ├── skills.md
│   └── assess.md
├── skills/                            # Skill modules
│   ├── frontend/SKILL.md
│   ├── backend/SKILL.md
│   ├── devops/SKILL.md
│   ├── data-ai/SKILL.md
│   ├── languages/SKILL.md
│   ├── architecture/SKILL.md
│   └── security/SKILL.md
├── hooks/
│   └── hooks.json                     # Automation hooks
└── README.md
```

## 📚 Covered Roadmaps (65+)

### Frontend (14 roles)
HTML, CSS, JavaScript, TypeScript, React, Next.js, Vue, Angular, React Native, Flutter, iOS, Android, SwiftUI, UX Design

### Backend (11 roles)
Backend, Node.js, Python, Java, Go, Rust, PHP, Spring Boot, ASP.NET Core, GraphQL, API Design

### DevOps (8 roles)
DevOps, Docker, Kubernetes, Terraform, AWS, Google Cloud, Linux, Bash/Shell

### Data Science & AI (10 roles)
AI Data Scientist, AI Engineer, ML, MLOps, Data Analyst, BI Analyst, Data Engineer, Prompt Engineering, AI Red Teaming, AI Agents

### Languages (11 roles)
JavaScript, TypeScript, Python, Java, Go, Rust, C++, Kotlin, Bash, Computer Science, DSA

### Architecture (7 roles)
Software Architect, System Design, Design & Architecture, Design System, Full Stack, Game Dev, Server-Side Game Dev

### Security & Specialized (7 roles)
Cybersecurity, Blockchain, PostgreSQL, MongoDB, Redis, SQL, Git & GitHub, PM, Engineering Manager, QA, Technical Writer, DevRel

## 🔄 Parallel Agent Analysis

All 7 agents work together in parallel to provide comprehensive guidance from multiple perspectives!

## 📊 Plugin Statistics

| Component | Count | Status |
|-----------|-------|--------|
| Agents | 7 | ✅ Active |
| Commands | 4 | ✅ Ready |
| Skills | 7 | ✅ Complete |
| Covered Roles | 65+ | ✅ Comprehensive |

---

**Happy Learning! 🎓**
