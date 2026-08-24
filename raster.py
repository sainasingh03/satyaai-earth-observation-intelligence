from pathlib import Path

import rasterio


def read_raster(path: str):

    file = Path(path)

    if not file.exists():
        raise FileNotFoundError(path)

    with rasterio.open(path) as src:

        return {
            "width": src.width,
            "height": src.height,
            "bands": src.count,
            "crs": str(src.crs),
            "bounds": {
                "left": src.bounds.left,
                "bottom": src.bounds.bottom,
                "right": src.bounds.right,
                "top": src.bounds.top,
            },
            "transform": src.transform,
        }