#!/usr/bin/env python3
"""Memory and Cache Analysis Simulator."""

import json
from collections import OrderedDict
from typing import List


class LRUCache:
    """LRU Cache implementation for page replacement simulation."""

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()
        self.hits = 0
        self.misses = 0

    def access(self, page: int) -> bool:
        """Access a page, return True if hit, False if miss."""
        if page in self.cache:
            self.cache.move_to_end(page)
            self.hits += 1
            return True
        else:
            if len(self.cache) >= self.capacity:
                self.cache.popitem(last=False)
            self.cache[page] = True
            self.misses += 1
            return False

    def get_stats(self) -> dict:
        total = self.hits + self.misses
        return {
            "hits": self.hits,
            "misses": self.misses,
            "hit_rate": self.hits / total if total > 0 else 0,
            "miss_rate": self.misses / total if total > 0 else 0
        }


def simulate_page_access(pages: List[int], cache_size: int) -> dict:
    """Simulate LRU page replacement."""
    cache = LRUCache(cache_size)

    access_log = []
    for page in pages:
        hit = cache.access(page)
        access_log.append({"page": page, "hit": hit})

    return {
        "cache_size": cache_size,
        "total_accesses": len(pages),
        "stats": cache.get_stats(),
        "final_cache": list(cache.cache.keys()),
        "access_log": access_log[:10]  # First 10 for brevity
    }


def analyze_locality(pages: List[int]) -> dict:
    """Analyze temporal and spatial locality."""
    # Temporal: same page accessed again
    temporal_reuse = sum(
        1 for i, p in enumerate(pages[1:], 1)
        if p in pages[:i]
    )

    # Spatial: adjacent pages
    spatial = sum(
        1 for i in range(1, len(pages))
        if abs(pages[i] - pages[i-1]) <= 1
    )

    return {
        "temporal_locality": temporal_reuse / len(pages) if pages else 0,
        "spatial_locality": spatial / len(pages) if pages else 0,
        "locality_score": (temporal_reuse + spatial) / (2 * len(pages)) if pages else 0
    }


def main():
    # Example simulation
    pages = [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5]
    result = simulate_page_access(pages, cache_size=3)
    result["locality"] = analyze_locality(pages)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
