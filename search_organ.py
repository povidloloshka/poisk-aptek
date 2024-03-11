import requests


def find_business(ll, spn, request, locale='ru_RU'):
    search_api_server = 'https://search-maps.yandex.ru/v1/'
    API_KEY = 'dda3ddba-c9ea-4ead-9010-f43fbc15c6e3'
    params = {
        'apikey': API_KEY,
        'text': request,
        'lang': locale,
        'll': ll,
        'spn': spn,
        'type': 'biz'
    }
    response = requests.get(search_api_server, params=params)
    if not response:
        pass
    json_response = response.json()
    organizations = json_response['features']
    return organizations


def get_business(ll, spn, request, locale='ru_Ru'):
    args = find_business(ll, spn, request, locale=locale)
    if args:
        return args[0]
