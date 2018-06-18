from urllib.request import urlopen
from urllib.parse import quote
from bs4 import BeautifulSoup

def fetch_data_from_url(url):
    with urlopen(url) as fp:
        data = fp.read()
    obj = BeautifulSoup(data,"html.parser")
    return obj


def scrap_required_data(soup):
    lines = soup.text.split('\n')
    lines = map(str.strip,lines)
    lines = [i for i in filter( lambda i:i!='', lines)]
    
    today = lines[:lines.index("7 Day's Forecast")]
    forecast = lines[lines.index("7 Day's Forecast"):]
    
    forecast.remove("7 Day's Forecast")
    iforecast = iter(forecast)
    fcs = []
    for date,mintemp,maxtemp,weather in zip(iforecast,iforecast,iforecast,iforecast):
        fcs.append((date,mintemp,maxtemp,weather))

    itoday = iter(today)
    ty = {}
    for key,val in zip(itoday,itoday):
        ty[key] = val
    ty.pop("Local Weather Report and Forecast")
    
    return ty,fcs


def get_cities():
    url = "http://www.imd.gov.in/pages/city_weather_main.php"
    soup = fetch_data_from_url(url)
    options = soup.findAll("form")[0].findAll("option")
    cities = [i.attrs['value'] for i in options]
    return cities

def get_city_from_user():
    city_list = get_cities()
    for ind,val in enumerate(city_list):
        print(ind,":",val)
    city = input("Please enter the city from the list: ")
    while city not in city_list:
        city = input("Please enter a valid input")
    return city

def get_city_url(city):
    city = quote(city)
    url = "http://www.imd.gov.in/pages/city_weather_main.php"
    soup = fetch_data_from_url(url)
    action = soup.findAll("form")[0].attrs['action']
    data = "obs_name={city}&submit=Go".format(city=city)
    string = urlopen("http://www.imd.gov.in/pages/city_weather_show.php", data=bytes(data,'utf-8')).read()
    soup = BeautifulSoup(string,'html.parser')
    return soup.findAll("iframe")[0].attrs['src']



def get_city_weather(cityname):
    url = get_city_url(cityname)
    soup = fetch_data_from_url(url)
    return scrap_required_data(soup)
    

if __name__ == "__main__":
    # this url is specific for chennai location. For other stations a different url is needed
    city4 = "CHENNAI (NUNGAMBAKKAM)"
    city1 = "NEW DELHI (SAFDARJUNG)"
    city2 = "MUMBAI (SANTACRUZ) (A)"
    city3 = "KOLKATA"
    url = get_city_url(city2)
    soup = fetch_data_from_url(url)
    today,forecast = scrap_required_data(soup)
    for day in forecast:
        print(day[0],"\t",day[3])
    
    
    
    
        
        
    
