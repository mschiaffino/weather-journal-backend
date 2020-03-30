from city_name import fetch_city_name, get_named_city


def test_fetch_city_name():
    coordinates_query_param = 's=32.8895&w=68.8458'

    city_name = fetch_city_name(coordinates_query_param)

    assert city_name == 'Mendoza, Argentina'


def test_get_named_city():
    city = {
        'coordinates': 'n=51.5074&w=0.1278',
        'wind': '7 kph'
    }

    named_city = get_named_city(city)

    assert named_city['name'] == 'London, United Kingdom'
    assert named_city['wind'] == city['wind']
