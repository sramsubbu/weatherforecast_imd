import argparse
import sys
# from .weather_forecast import get_city_weather,get_cities
from imd_interface import get_city_weather, get_cities

EXIT_SUCCESS = 0
EXIT_INVALID_ARG = 1
EXIT_ERROR_PROCESSING = 2
EXIT_ERROR_UNKNOWN = 3


def build_parser():
    parser = argparse.ArgumentParser(description="Fetch weather information from IMD")
    parser.add_argument('-c' ,'--city', default='chennai (nungambakkam)')
    parser.add_argument('-l', '--list-cities',action='store_true')
    parser.add_argument('-f', '--forecast',action='store_true')
    return parser


def parse_args(parser):
    pass
    

def list_cities():
    cities = get_cities()
    for city in cities:
        print(city)

def get_city_forecast(city):
    today, forecast = get_city_weather(city)
    return today, forecast
        

def is_valid_city(city):
    cities = get_cities()
    return city in cities


def _pretty_print_dictionary(dct):
    keys = dct.keys()
    key_lens = (len(item) for item in keys)
    max_len = max(key_lens)

    for key, value in dct.items():
        print(f"{key:<{max_len}}   : {value}")
    


def main():
    parser = build_parser()
    args = parser.parse_args()
    
    if args.list_cities:
        # print cities and exit
        list_cities()
        sys.exit(EXIT_SUCCESS)
        
    cities = get_cities()
    city = args.city.upper()
    if not is_valid_city(city):
        print("The provided city is not valid.")
        sys.exit(EXIT_INVALID_ARG)
    city_id = cities[city]
    
    today, forecast = get_city_weather(city, city_id)
    if args.forecast:
        print("Forecase for the week")
        for day in forecast:
            print(day)
    else:
        print("Today's weather:")
        print("*"*25)
        print()
        _pretty_print_dictionary(today)
        


if __name__ == "__main__":
    main()

