"""Wind rose data loading and processing."""

import numpy as np
import pandas as pd
from typing import Dict, Tuple


def load_windrose(filepath: str) -> Dict[str, np.ndarray]:
    """
    Load wind rose CSV with columns: direction, speed, frequency.
    Returns dict with normalized frequency distribution.
    """
    df = pd.read_csv(filepath)
    required = {"direction", "speed", "frequency"}
    if not required.issubset(df.columns):
        raise ValueError(f"CSV must contain columns: {required}")

    freq = df["frequency"].values
    freq = freq / freq.sum()  # normalize

    return {
        "direction": np.radians(df["direction"].values),
        "speed": df["speed"].values,
        "frequency": freq,
    }


def dominant_direction(wind_data: Dict[str, np.ndarray]) -> float:
    """Return the most frequent wind direction in radians."""
    idx = np.argmax(wind_data["frequency"])
    return wind_data["direction"][idx]