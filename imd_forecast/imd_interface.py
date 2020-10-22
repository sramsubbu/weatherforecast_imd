import requests
import bs4
from bs4 import BeautifulSoup

CITY_LIST_URL="https://internal.imd.gov.in/pages/city_weather_main_mausam.php"
CITY_FORECASE_URL = "https://city.imd.gov.in/citywx/city_weather.php"

def get_cities():
    resp = requests.get(CITY_LIST_URL)
    soup = BeautifulSoup(resp.text, "html.parser")
    city_tags = list(soup.find_all('datalist')[0].children)
    city_tags = [item for item in city_tags if isinstance(item,
                                            bs4.element.Tag)]
    city_dict = {}
    for city_tag in city_tags:
        value = city_tag.attrs['value'].strip()
        name = city_tag.text.strip()
        city_dict[name] = value
        
    return city_dict


def get_city_weather(city_name, city_id):
    data = {
        'id': city_id
    }
    resp = requests.post(CITY_FORECASE_URL, data=data)
    soup = BeautifulSoup(resp.text, "html.parser")

    # clean the dataset
    lines = soup.text.split("\n")
    lines = [line.strip() for line in lines]
    lines = [i for i in lines if i != '']

    # split the data into today's data and forecast data.
    split_index = lines.index("7 Day's Forecast")
    today = lines[:split_index]
    forecast = lines[split_index+1:]
    fcs = [forecast[i:i+4] for i in range(0, len(forecast), 4)]
    
    itoday = iter(today)
    ty = dict(zip(itoday, itoday))
    ty.pop("Local Weather Report and Forecast")
    return ty, fcs
    
if __name__ == '__main__':
    cities = get_cities()
    city_name = 'CHENNAI (NUNGAMBAKKAM)'
    city_id = cities[city_name]
    res = get_city_weather(city_name, city_id)
    print(res)
    
