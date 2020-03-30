import requests
from flask_restful import Resource

from scrapper.scrapper import scrape_data
from utils.city_name import get_named_city

STATIC_WEBSITE_URL = 'https://app.deta.sh/hw6g4zdvlmao/'


class CitiesResource(Resource):
    def get(self):
        site_response = requests.get(STATIC_WEBSITE_URL)
        scraped_data = scrape_data(site_response.content)

        cities = [get_named_city(city) for city in scraped_data]

        return cities
