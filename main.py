import sys
from geo import get_сoordinates
from map_pg import show_map
from organisation_search import get_business
from distance import lonlat_distance


def main():
    toponym_to_find = ' '.join(sys.argv[1:])
    lat, lon = get_сoordinates(toponym_to_find)
    address_ll = f'{lat},{lon}'
    span = '0.005,0.005'
    organization = get_business(address_ll, span, 'аптека')
    point = organization['geometry']['coordinates']
    org_lat = float(point[0])
    org_lon = float(point[1])
    point_param = f'pt={org_lat},{org_lon},pm2dgl'
    points_param = point_param + f'~{address_ll},pm2rdl'
    show_map(map_type='map', add_params=points_param)
    name = organization['properties']['CompanyMetaData']['name']
    address = organization['properties']['CompanyMetaData']['address']
    time = organization['properties']['CompanyMetaData']['Hours']['text']
    distance = round(lonlat_distance((lon, lat), (org_lon, org_lat)))

    snippet = f'Название:\t{name}\nАдрес:\t{address}\nВремя работы:\t{time}\n' \
              f'Расстояние:\t{distance}м.'
    print(snippet)


if __name__ == '__main__':
    main()
