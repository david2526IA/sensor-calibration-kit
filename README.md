# Sensor Calibration Kit

Offline analysis for linear sensor calibration data. Given reference and measured values, it fits:

`reference = slope × measured + offset`

and returns RMSE plus every residual for review and traceability.

## Run

`points.json`:

```json
[{"measured":0.0,"reference":1.0},{"measured":2.0,"reference":5.0}]
```

```bash
pip install .
sensor-calibrate points.json --output calibration_report.json
```

## Scope and limits

This is a calculation aid, not a calibration procedure or instrument-control system. It does not write to a PLC, sensor or controller. Review measurement uncertainty, applicable procedures, environmental conditions and qualified approval before applying any adjustment.

## Development

```bash
pip install ".[dev]"
pytest -q
```

## License

MIT
