from __future__ import annotations

import argparse
import json
from pathlib import Path

from .linear import fit_calibration


def main() -> None:
    parser = argparse.ArgumentParser(description="Fit an offline linear sensor calibration model.")
    parser.add_argument("points", type=Path, help="JSON array of measured/reference calibration points")
    parser.add_argument("--output", type=Path, default=Path("calibration_report.json"))
    args = parser.parse_args()
    report = fit_calibration(json.loads(args.points.read_text(encoding="utf-8")))
    args.output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: report[key] for key in ("slope", "offset", "rmse", "points")}))
