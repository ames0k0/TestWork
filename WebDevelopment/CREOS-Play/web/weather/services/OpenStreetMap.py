from OSMPythonTools.overpass import Overpass

from ..models import City


CITY_NOT_FOUND = "{CITY_NAME} не найдено!"


overpass = Overpass()


def get_city_lat_and_long(city_name: str) -> tuple | None:
    result = overpass.query(f'way["name"="{city_name}"]; out body;')
    for city_name in result.elements():
        for node in city_name.nodes():
            return node.lat(), node.lon()


def init_city(city_name: str) -> tuple[str, City | None]:
    data = get_city_lat_and_long(city_name)
    if not data:
        return CITY_NOT_FOUND.format(city_name).title(), None

    city = City(
        name=city_name,
        latitude=data[0],
        longitude=data[1],
    )
    city.save()

    return "", city