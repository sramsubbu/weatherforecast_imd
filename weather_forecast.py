from urllib.request import urlopen
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
            


if __name__ == "__main__":
    # this url is specific for chennai location. For other stations a different url is needed
    url = "http://city.imd.gov.in/citywx/city_weather.php?id=43279"
    soup = fetch_data_from_url(url)
    today,forecast = scrap_required_data(soup)
    for day in forecast:
        print(day[0],"\t",day[3])
        
        
    
