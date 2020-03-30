import concurrent.futures

import requests
from flask_restful import Resource

from scrapper.scrapper import scrape_data
from utils.city_name import get_named_city

from schemas.city_schema import CitySchema

STATIC_WEBSITE_URL = 'https://app.deta.sh/hw6g4zdvlmao/'


class CitiesResource(Resource):
    def get(self):
        site_response = requests.get(STATIC_WEBSITE_URL)
        scraped_data = scrape_data(site_response.content)

        with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
            cities = list(executor.map(get_named_city, scraped_data))

            return CitySchema().dump(cities, many=True)
