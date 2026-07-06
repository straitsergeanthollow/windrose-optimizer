"""Tests for windrose_optimizer package."""

import numpy as np
import tempfile
import os
from windrose_optimizer import load_windrose, compute_yield, optimize_layout


def test_load_windrose():
    """Test loading a valid wind rose CSV."""
    csv_content = "direction,speed,frequency\n0,5,0.3\n90,10,0.5\n180,15,0.2\n"
    with tempfile.NamedTemporaryFile(mode="w", suffix=".csv", delete=False) as f:
        f.write(csv_content)
        tmp_path = f.name

    try:
        data = load_windrose(tmp_path)
        assert "direction" in data
        assert "speed" in data
        assert "frequency" in data
        assert np.isclose(data["frequency"].sum(), 1.0)
    finally:
        os.unlink(tmp_path)


def test_compute_yield():
    """Test yield computation returns positive value."""
    wind_data = {
        "direction": np.array([0.0, np.pi / 2]),
        "speed": np.array([10.0, 5.0]),
        "frequency": np.array([0.5, 0.5]),
    }
    yield_mwh = compute_yield(wind_data)
    assert yield_mwh > 0
    assert isinstance(yield_mwh, float)


def test_optimize_layout():
    """Test optimizer returns correct number of positions."""
    wind_data = {
        "direction": np.array([0.0]),
        "speed": np.array([12.0]),
        "frequency": np.array([1.0]),
    }
    positions = optimize_layout(wind_data, n_turbines=3, generations=5, pop_size=20)
    assert len(positions) == 3
    for x, y in positions:
        assert 0 <= x <= 1000
        assert 0 <= y <= 1000