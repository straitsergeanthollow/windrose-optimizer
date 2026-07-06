"""Genetic algorithm optimizer for turbine layout."""

import numpy as np
from typing import List, Tuple
from .yield_model import compute_yield
from .windrose import load_windrose


def optimize_layout(
    wind_data: dict,
    n_turbines: int = 5,
    bounds: Tuple[float, float, float, float] = (0, 1000, 0, 1000),
    generations: int = 50,
    pop_size: int = 100,
) -> List[Tuple[float, float]]:
    """
    Simple genetic algorithm to find optimal turbine positions.
    Maximizes total yield (simplified: no wake effects).
    """
    xmin, xmax, ymin, ymax = bounds
    n_vars = n_turbines * 2

    # Initialize population
    pop = np.random.uniform(
        [xmin, ymin] * n_turbines,
        [xmax, ymax] * n_turbines,
        (pop_size, n_vars),
    )

    def fitness(individual):
        positions = individual.reshape(-1, 2)
        # Simple penalty for too-close turbines
        penalty = 0
        for i in range(n_turbines):
            for j in range(i + 1, n_turbines):
                dist = np.linalg.norm(positions[i] - positions[j])
                if dist < 100:
                    penalty += (100 - dist) * 100
        # Each turbine contributes same yield (simplified)
        base_yield = compute_yield(wind_data) * n_turbines
        return base_yield - penalty

    for gen in range(generations):
        scores = np.array([fitness(ind) for ind in pop])
        # Select top half
        idx = np.argsort(scores)[-pop_size // 2 :]
        parents = pop[idx]

        # Crossover
        children = []
        for _ in range(pop_size - len(parents)):
            p1, p2 = parents[np.random.randint(0, len(parents), 2)]
            mask = np.random.rand(n_vars) > 0.5
            child = np.where(mask, p1, p2)
            # Mutation
            if np.random.rand() < 0.1:
                child += np.random.normal(0, 50, n_vars)
            children.append(child)

        pop = np.vstack([parents, children])

    # Best individual
    best_idx = np.argmax([fitness(ind) for ind in pop])
    best = pop[best_idx].reshape(-1, 2)
    return [(float(x), float(y)) for x, y in best]