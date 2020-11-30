import requests


def printWeather(ans):
    print("Main\t:\t" + ans['weather'][0]['main'] + "\nDescription\t:\t" + ans['weather'][0]['description'] + "\n")


def printWind(ans):
    print("Speed\t:\t" + str(ans['wind']['speed']) + "\nDirection\t:\t" + str(ans['wind']['deg']) + "\n")


def printPressure(ans):
    print("Pressure\n\tSea Level\t:\t" + str(ans['main']['sea_level']) + "\n\tGround Level\t:\t" + str(
        ans['main']['grnd_level']) + "\n")


def callApi(choice, query):
    url = 'https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22'
    jsonResponse = requests.get(url)
    Response = jsonResponse.json()
    lis = Response['list']

    for ans in lis:
        if ans['dt_txt'] == query:
            break;

    if choice == '1':
        printWeather(ans)
    elif choice == '2':
        printWind(ans)
    elif choice == '3':
        printPressure(ans)
    else:
        print('Data not Found\n')


def core():
    while True:
        choice = input('input choice 1, 2, 3, 0 : ')
        if choice == '0':
            break

        usrin = input('Enter your date (yyyy-mm-dd): ')
        query = input('Enter time (00:00:00):')

        fquery=usrin+" "+query
        callApi(choice, fquery)


if __name__ == '__main__':
    core()

'''
{
"cod":"200",
"message":0.0151,
"cnt":96,
"list":[
    {
        "dt":1553709600,
        "main":
        {
            "temp":278.76,
            "temp_min":278.76,
            "temp_max":279.558,
            "pressure":1031.934,
            "sea_level":1031.934,
            "grnd_level":971.745,
            "humidity":100,
            "temp_kf":-0.8
        },
        "weather":[
            {
                "id":803,
                "main":"Clouds",
                "description":"brokenclouds",
                "icon":"04n"    
            }
        ],
        "clouds":
        {
            "all":77
        },
        "wind":
        {
            "speed":1.6,
            "deg":40.932
        },
        "sys":
        {
            "pod":"n"
        },
        "dt_txt":"2019-03-27 18:00:00"
    },
    {
        ...
    }
]
}
'''


