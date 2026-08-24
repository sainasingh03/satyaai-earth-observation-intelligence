import numpy as np


def calculate_ndvi(
    nir: np.ndarray,
    red: np.ndarray,
) -> np.ndarray:

    nir = nir.astype(np.float32)
    red = red.astype(np.float32)

    denominator = nir + red

    ndvi = np.divide(
        nir - red,
        denominator,
        out=np.zeros_like(nir),
        where=denominator != 0,
    )

    return np.clip(
        ndvi,
        -1.0,
        1.0,
    )