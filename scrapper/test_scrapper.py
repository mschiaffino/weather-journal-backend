from scrapper import parse_coordinates


def test_parse_coordinates():
    coordinates = '33.8688° S, 151.2093° E'

    parsed_coordinates = parse_coordinates(coordinates)

    assert parsed_coordinates == 's=33.8688&e=151.2093'
