"""Least-squares linear calibration and residual analysis."""

from __future__ import annotations

import math
from typing import Any


def fit_calibration(points: list[dict[str, float]]) -> dict[str, Any]:
    """Fit ``reference = slope * measured + offset`` to calibration points."""
    if len(points) < 2:
        raise ValueError("at least two calibration points are required")
    measured = [point.get("measured") for point in points]
    reference = [point.get("reference") for point in points]
    if not all(isinstance(value, (int, float)) and math.isfinite(value) for value in measured + reference):
        raise ValueError("each point requires finite measured and reference values")
    mean_x = sum(measured) / len(measured)
    mean_y = sum(reference) / len(reference)
    denominator = sum((value - mean_x) ** 2 for value in measured)
    if denominator == 0:
        raise ValueError("measured values must not all be identical")
    slope = sum((x - mean_x) * (y - mean_y) for x, y in zip(measured, reference)) / denominator
    offset = mean_y - slope * mean_x
    residuals = []
    for index, (x, y) in enumerate(zip(measured, reference)):
        predicted = slope * x + offset
        residuals.append({"index": index, "measured": x, "reference": y, "predicted": round(predicted, 8), "residual": round(y - predicted, 8)})
    rmse = math.sqrt(sum(item["residual"] ** 2 for item in residuals) / len(residuals))
    return {
        "model": "reference = slope * measured + offset",
        "slope": round(slope, 8),
        "offset": round(offset, 8),
        "points": len(points),
        "rmse": round(rmse, 8),
        "residuals": residuals,
        "scope": "analysis only; review against the instrument procedure before applying any adjustment",
    }
