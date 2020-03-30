import requests

CITY_NAMES_API_URL = 'https://app.deta.sh/hw6g4zdvlmao/lookup'


def fetch_city_name(coordinates_query_param):
    url = f'{CITY_NAMES_API_URL}?{coordinates_query_param}'
    response = requests.get(url)
    city_name = response.json().get('result')

    return city_name


def get_named_city(city):
    coordinates_query_param = city.get('coordinates')
    city_name = fetch_city_name(coordinates_query_param)

    return {**city, 'name': city_name}
