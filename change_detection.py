import numpy as np


def calculate_change(
    before: np.ndarray,
    after: np.ndarray,
) -> np.ndarray:

    return (
        after.astype(np.float32)
        - before.astype(np.float32)
    )


def detect_loss(
    before: np.ndarray,
    after: np.ndarray,
    threshold: float = -0.15,
) -> np.ndarray:

    change = calculate_change(
        before,
        after,
    )

    return change <= threshold


def loss_percentage(
    before: np.ndarray,
    after: np.ndarray,
    threshold: float = -0.15,
) -> float:

    mask = detect_loss(
        before,
        after,
        threshold,
    )

    return float(mask.mean() * 100)