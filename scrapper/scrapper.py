import re
from bs4 import BeautifulSoup

COORDINATES_REGEX = (r'(\d{1,2}\.\d{1,4})°\s([SN]),\s'
                     r'(\d{1,3}\.\d{1,4})°\s([EW])')


def parse_coordinates(coordinates):
    """
    Returns the parsed coordinates to be used as query string.
    """
    search_results = re.search(COORDINATES_REGEX, coordinates)
    groups_found = search_results.groups()

    latitude_angle = groups_found[0]
    latitude_hemisphere = groups_found[1].lower()
    longitude_angle = groups_found[2]
    longitude_hemisphere = groups_found[3].lower()

    parsed_coordinates = (f'{latitude_hemisphere}={latitude_angle}'
                          f'&{longitude_hemisphere}={longitude_angle}')

    return parsed_coordinates


def scrape_data(html):
    """
    Returns a list of dictionaries with the parsed cities coordinates and wind info.
    """
    soup = BeautifulSoup(html, features='html.parser')
    table = soup.find('table')
    table_rows = table.find_all('tr')

    data = []

    for tr in table_rows[1:]:  # skip table header
        tds = tr.find_all('td')

        coordinates = parse_coordinates(tds[0].text)
        wind = tds[1].text

        data.append({'coordinates': coordinates,
                     'wind': wind})

    return data
