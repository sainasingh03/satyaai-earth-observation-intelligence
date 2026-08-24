import numpy as np

from app.vision.ndvi import calculate_ndvi


def test_ndvi():

    nir = np.array(
        [[0.8, 0.7]]
    )

    red = np.array(
        [[0.2, 0.3]]
    )

    result = calculate_ndvi(
        nir,
        red,
    )

    assert result.shape == nir.shape
    assert result[0, 0] > 0