"""Simple wind turbine yield model based on wind rose."""

import numpy as np
from .windrose import load_windrose


def compute_yield(
    wind_data: dict,
    turbine_power_curve: list = None,
    hub_height: float = 80.0,
) -> float:
    """
    Estimate annual energy yield (MWh) from wind rose data.
    Uses a simplified power curve: P = 0.5 * rho * A * Cp * v^3
    """
    if turbine_power_curve is None:
        # Default: 2 MW turbine, cut-in 3 m/s, cut-out 25 m/s
        turbine_power_curve = [(3, 0), (12, 2000), (25, 2000)]

    rho = 1.225  # air density kg/m3
    rotor_area = np.pi * (50**2)  # 50m radius -> ~7854 m2
    cp = 0.45  # power coefficient

    speeds = wind_data["speed"]
    freqs = wind_data["frequency"]
    hours_per_year = 8760

    # Simple power per speed bin
    power = np.where(
        (speeds >= 3) & (speeds <= 25),
        0.5 * rho * rotor_area * cp * (speeds**3) / 1e6,  # MW
        0,
    )

    annual_yield = np.sum(power * freqs) * hours_per_year
    return float(annual_yield)