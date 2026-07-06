# Windrose Optimizer

Optimizes wind turbine placement using wind rose data to maximize energy yield.

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```python
from windrose_optimizer import load_windrose, compute_yield, optimize_layout

wind_data = load_windrose("data/wind_rose.csv")
best_positions = optimize_layout(wind_data, n_turbines=5)
print(best_positions)
```

## Testing

```bash
pytest tests/
```