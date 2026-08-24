from shapely.geometry import Point


def create_point(
    latitude: float,
    longitude: float,
):

    return Point(
        longitude,
        latitude,
    )