from scrapper import parse_coordinates, scrape_data

MOCKED_SITE_FILE_PATH = 'mocks/mocked_static_site.html'


def test_parse_coordinates():
    coordinates = '33.8688° S, 151.2093° E'

    parsed_coordinates = parse_coordinates(coordinates)

    assert parsed_coordinates == 's=33.8688&e=151.2093'


def test_scrape_data():
    with open(MOCKED_SITE_FILE_PATH, 'r', encoding='utf-8') as site_html:
        scraped_data = scrape_data(site_html)

        assert len(scraped_data) == 10

        assert scraped_data[0].get('coordinates') == 'n=51.5074&w=0.1278'
        assert scraped_data[0].get('wind') == '47 kph'

        assert scraped_data[1].get('coordinates') == 'n=41.7151&e=44.827'
        assert scraped_data[1].get('wind') == '14 kph'

        assert scraped_data[4].get('coordinates') == 's=54.8019&w=68.3030'
        assert scraped_data[4].get('wind') == '15 kph'

        assert scraped_data[9].get('coordinates') == 's=1.2921&e=36.8219'
        assert scraped_data[9].get('wind') == '20 kph'
