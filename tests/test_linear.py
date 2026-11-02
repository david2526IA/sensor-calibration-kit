import pytest

from sensor_calibration_kit.linear import fit_calibration


def test_exact_linear_points_fit_expected_model() -> None:
    report = fit_calibration([{"measured": 0.0, "reference": 1.0}, {"measured": 2.0, "reference": 5.0}, {"measured": 4.0, "reference": 9.0}])
    assert report["slope"] == 2.0
    assert report["offset"] == 1.0
    assert report["rmse"] == 0.0


def test_residuals_are_retained_for_review() -> None:
    report = fit_calibration([{"measured": 0.0, "reference": 0.0}, {"measured": 1.0, "reference": 2.0}, {"measured": 2.0, "reference": 3.0}])
    assert len(report["residuals"]) == 3
    assert report["rmse"] > 0


def test_unusable_points_are_rejected() -> None:
    with pytest.raises(ValueError, match="identical"):
        fit_calibration([{"measured": 1.0, "reference": 2.0}, {"measured": 1.0, "reference": 3.0}])
