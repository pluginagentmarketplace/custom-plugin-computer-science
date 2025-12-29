#!/usr/bin/env python3
"""Data Structure Usage Analyzer."""

import re
import json
from pathlib import Path


DS_PATTERNS = {
    "array": [r"\[\]", r"list\(", r"np\.array", r"Array\("],
    "linked_list": [r"ListNode", r"\.next", r"head\s*=", r"LinkedList"],
    "stack": [r"\.push\(", r"\.pop\(", r"Stack\(", r"LIFO"],
    "queue": [r"deque\(", r"Queue\(", r"\.enqueue", r"FIFO"],
    "hash_map": [r"dict\(", r"\{\}", r"HashMap", r"\.get\(.*,"],
    "set": [r"set\(", r"HashSet", r"\.add\("],
    "tree": [r"TreeNode", r"\.left", r"\.right", r"root\s*="],
    "heap": [r"heapq", r"PriorityQueue", r"heappush", r"heappop"],
    "graph": [r"adjacency", r"neighbors", r"edges", r"Graph\("],
}


def analyze_data_structures(code: str) -> dict:
    """Detect data structures used in code."""
    detected = {}

    for ds_name, patterns in DS_PATTERNS.items():
        for pattern in patterns:
            if re.search(pattern, code, re.IGNORECASE):
                detected[ds_name] = detected.get(ds_name, 0) + 1

    # Recommend based on usage
    recommendations = []
    if "array" in detected and detected.get("array", 0) > 5:
        recommendations.append("Consider using numpy for large arrays")
    if "linked_list" in detected:
        recommendations.append("Verify O(1) insertion is needed vs array")
    if "hash_map" in detected:
        recommendations.append("Good choice for O(1) lookups")

    return {
        "detected_structures": detected,
        "primary_structure": max(detected, key=detected.get) if detected else None,
        "recommendations": recommendations,
        "complexity_profile": "optimized" if "hash_map" in detected or "heap" in detected else "standard"
    }


def main():
    import sys
    if len(sys.argv) > 1:
        code = Path(sys.argv[1]).read_text()
    else:
        code = sys.stdin.read()
    print(json.dumps(analyze_data_structures(code), indent=2))


if __name__ == "__main__":
    main()
