import re

COORDINATES_REGEX = (r'(\d{1,2}\.\d{1,4})°\s([SN]),\s'
                     r'(\d{1,3}\.\d{1,4})°\s([EW])')


def parse_coordinates(coordinates):
    search_results = re.search(COORDINATES_REGEX, coordinates)
    groups_found = search_results.groups()

    latitude_angle = groups_found[0]
    latitude_hemisphere = groups_found[1].lower()
    longitude_angle = groups_found[2]
    longitude_hemisphere = groups_found[3].lower()

    parsed_coordinates = (f'{latitude_hemisphere}={latitude_angle}'
                          f'&{longitude_hemisphere}={longitude_angle}')

    return parsed_coordinates
