import requests
import pandas as pd
import datetime

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
        "region": responseJson['location']['region'],
        "country": responseJson['location']['country'],
        "temperatureC":responseJson['current']['temp_c'],
        "UV":responseJson['current']['uv'],
        "precipitation":responseJson['current']['precip_mm']
    }
    return returnedData

def readWriteDataWeather():
    df=pd.read_csv('cities.csv')
    dfList=[]
    for index, cities in df.iterrows():
        weatherData=getWeatherData(cities['CityName'])
        weatherData["City name"]=cities['CityName']
        dfList.append(weatherData)
    df2=pd.json_normalize(dfList)
    fileName="WEATHER_DATA"+datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")+".csv"
    df2.to_csv(fileName)

if __name__ == '__main__':
    readWriteDataWeather()