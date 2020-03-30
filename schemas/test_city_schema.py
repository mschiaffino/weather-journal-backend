from city_schema import CitySchema


def test_city_schema():
    city = {
        'coordinates': 'n=51.5074&w=0.1278',
        'wind': '7 kph',
        'name': 'London, United Kingdom'
    }

    city_dump = CitySchema().dump(city)

    assert city_dump['name'] == city['name']
    assert city_dump['wind'] == city['wind']
    assert 'coordinates' not in city_dump
