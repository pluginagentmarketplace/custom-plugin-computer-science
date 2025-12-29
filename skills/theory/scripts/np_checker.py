#!/usr/bin/env python3
"""NP-Completeness Problem Analyzer."""

import json
from typing import List, Dict


NP_COMPLETE_PROBLEMS = {
    "sat": {"name": "Boolean Satisfiability", "category": "logic"},
    "3sat": {"name": "3-SAT", "category": "logic"},
    "clique": {"name": "Clique Problem", "category": "graph"},
    "vertex_cover": {"name": "Vertex Cover", "category": "graph"},
    "hamiltonian": {"name": "Hamiltonian Path/Cycle", "category": "graph"},
    "tsp": {"name": "Traveling Salesman", "category": "optimization"},
    "subset_sum": {"name": "Subset Sum", "category": "number"},
    "knapsack": {"name": "0/1 Knapsack", "category": "optimization"},
    "graph_coloring": {"name": "Graph Coloring", "category": "graph"},
    "partition": {"name": "Partition Problem", "category": "number"},
}


def classify_problem(description: str) -> dict:
    """Classify a problem based on its description."""
    description_lower = description.lower()

    detected = []
    for key, info in NP_COMPLETE_PROBLEMS.items():
        if key.replace("_", " ") in description_lower or info["name"].lower() in description_lower:
            detected.append(info)

    # Heuristic detection
    if "satisf" in description_lower or "boolean" in description_lower:
        detected.append(NP_COMPLETE_PROBLEMS["sat"])
    if "travel" in description_lower or "shortest tour" in description_lower:
        detected.append(NP_COMPLETE_PROBLEMS["tsp"])
    if "knapsack" in description_lower or "capacity" in description_lower:
        detected.append(NP_COMPLETE_PROBLEMS["knapsack"])

    # Remove duplicates
    unique_detected = list({d["name"]: d for d in detected}.values())

    return {
        "detected_np_problems": unique_detected,
        "is_likely_np": len(unique_detected) > 0,
        "complexity_class": "NP-Complete" if unique_detected else "Unknown",
        "recommendation": "Consider approximation algorithms" if unique_detected else "May be in P"
    }


def main():
    import sys
    description = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else sys.stdin.read()
    print(json.dumps(classify_problem(description), indent=2))


if __name__ == "__main__":
    main()
