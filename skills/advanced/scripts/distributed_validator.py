#!/usr/bin/env python3
"""Distributed Systems Design Validator."""

import json
from typing import Dict, List


CAP_COMBINATIONS = {
    ("C", "A"): {
        "name": "CA",
        "example": "Traditional RDBMS",
        "note": "Fails during partition"
    },
    ("C", "P"): {
        "name": "CP",
        "example": "MongoDB, HBase, Redis",
        "note": "May refuse writes during partition"
    },
    ("A", "P"): {
        "name": "AP",
        "example": "Cassandra, CouchDB, DynamoDB",
        "note": "May return stale data"
    }
}


def analyze_system_design(requirements: Dict) -> dict:
    """Analyze distributed system design choices."""

    # Determine CAP preference
    needs_strong_consistency = requirements.get("strong_consistency", False)
    needs_high_availability = requirements.get("high_availability", False)
    needs_partition_tolerance = requirements.get("partition_tolerance", True)  # Usually required

    cap_choice = []
    if needs_strong_consistency:
        cap_choice.append("C")
    if needs_high_availability:
        cap_choice.append("A")
    if needs_partition_tolerance:
        cap_choice.append("P")

    # CAP theorem constraint
    if len(cap_choice) > 2:
        warning = "CAP theorem: Cannot have all three. Choose C+P or A+P."
    else:
        warning = None

    # Recommend technologies
    recommendations = []
    if "C" in cap_choice and "P" in cap_choice:
        recommendations = ["MongoDB", "PostgreSQL with replication", "etcd"]
    elif "A" in cap_choice and "P" in cap_choice:
        recommendations = ["Cassandra", "DynamoDB", "CouchDB"]

    # Consensus algorithm recommendation
    if requirements.get("consensus_needed", False):
        consensus = "Raft (simpler) or Paxos (battle-tested)"
    else:
        consensus = "Not required for this design"

    return {
        "cap_choice": cap_choice,
        "cap_warning": warning,
        "recommendations": recommendations,
        "consensus_algorithm": consensus,
        "scalability": "horizontal" if "P" in cap_choice else "vertical",
        "data_model": "eventual" if "A" in cap_choice and "P" in cap_choice else "strong"
    }


def main():
    # Example analysis
    requirements = {
        "strong_consistency": True,
        "high_availability": True,
        "partition_tolerance": True,
        "consensus_needed": True
    }
    print(json.dumps(analyze_system_design(requirements), indent=2))


if __name__ == "__main__":
    main()
