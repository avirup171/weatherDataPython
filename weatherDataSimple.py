import requests

baseUrl = "http://api.weatherapi.com/v1/current.json"
key = "WEATHER API KEY"
location = "Shiliguri"

def getWeatherData(cityName):
    parameters = {
        'key':key,
        'q': cityName,
    }
    response = requests.get(baseUrl,params=parameters)
    responseJson=response.json()
    returnedData = {
        "CityName":cityName,
        "region": responseJson['location']['region'],
        "country": responseJson['location']['country'],
        "temperatureC":responseJson['current']['temp_c'],
        "UV":responseJson['current']['uv'],
        "precipitation":responseJson['current']['precip_mm']
    }
    return returnedData



if __name__ == '__main__':
    print(getWeatherData('Shiliguri'))