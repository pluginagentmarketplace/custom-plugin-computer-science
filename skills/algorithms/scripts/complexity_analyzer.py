#!/usr/bin/env python3
"""Algorithm Complexity Analyzer."""

import re
import json
from pathlib import Path


COMPLEXITY_PATTERNS = {
    # Loop patterns
    r"for\s+\w+\s+in\s+range\(n\)": "O(n)",
    r"for\s+\w+\s+in\s+range\(\w+\):\s*\n\s*for": "O(n²)",
    r"while\s+\w+\s*<\s*n": "O(n)",
    r"while\s+\w+\s*>\s*1:\s*\n.*//=\s*2": "O(log n)",

    # Recursion patterns
    r"def\s+\w+.*:\s*\n.*\w+\(n//2\)": "O(log n)",
    r"def\s+\w+.*:\s*\n.*\w+\(n-1\)": "O(n)",
    r"\w+\(n//2\).*\+.*\w+\(n//2\)": "O(n log n)",
}


def analyze_complexity(code: str) -> dict:
    """Analyze algorithm complexity from code."""
    detected = []
    code_lower = code.lower()

    for pattern, complexity in COMPLEXITY_PATTERNS.items():
        if re.search(pattern, code, re.MULTILINE | re.IGNORECASE):
            detected.append(complexity)

    # Count nested loops
    loop_depth = max(
        len(re.findall(r"for|while", line))
        for line in code.split("\n")
    ) if code else 0

    # Estimate based on loop depth
    if not detected:
        if loop_depth == 0:
            detected.append("O(1)")
        elif loop_depth == 1:
            detected.append("O(n)")
        elif loop_depth == 2:
            detected.append("O(n²)")
        elif loop_depth >= 3:
            detected.append("O(n³+)")

    return {
        "detected_complexities": list(set(detected)),
        "loop_depth": loop_depth,
        "estimated_time": detected[0] if detected else "O(1)",
        "has_recursion": "def" in code and re.search(r"return.*\w+\(", code) is not None
    }


def main():
    import sys
    if len(sys.argv) > 1:
        code = Path(sys.argv[1]).read_text()
    else:
        code = sys.stdin.read()
    print(json.dumps(analyze_complexity(code), indent=2))


if __name__ == "__main__":
    main()
