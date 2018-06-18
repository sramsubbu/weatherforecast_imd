import argparse

from weather_forecast import get_city_weather,get_cities




if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fetch weather information from IMD")

    parser.add_argument('-c' ,'--city', default='chennai')
    parser.add_argument('-l', '--list',action='store_true')
    parser.add_argument('-f', '--forecast',action='store_true')

    args= parser.parse_args()

    print(args)

    if args.list:
        cities = get_cities()
        for city in cities: print(city)
    else:
        cities = get_cities()
        if args.city in cities:
            today, forecast = get_city_weather(args.city)
            if args.forecast:
                print("Forecase for the week")
                for day in forecast:
                    print(day)
            else:
                print("Today's weather:")
                for item in  today:
                    print(f"{item} => {today[item]}")
        else:
            print(f"{args.city} is not a valid city")