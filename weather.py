import requests
def user_input():
    print('Select type of location:')
    loc_type = input('1. Geo Coordinates\n2. City Name\n')
    loc_type.strip()
    if loc_type=='1':
        try:
            lat = float(input('Enter latitude: '))
            lon = float(input('Enter Longitude: '))
        except:
            print('Enter valid values')
            return user_input()
    elif loc_type=='2':
        city = input('Enter the city name: ')
    else:
        print('Choose either 1 or 2')
        return user_input()
    
    return loc_type, {'lat':lat, 'lon':lon} if loc_type=='1' else {'q':city}

def main():
    key = '5aa28dc3a0a7959a197d61d527c52b7a'
    url = 'https://api.openweathermap.org/data/2.5/forecast'

    choice, loc = user_input()
    if choice=='1':
        r = requests.get(url, params={'appid':key, 'lat':loc['lat'], 'lon':loc['lon'], 'units':'metric'}, timeout=5)
    else:
        r = requests.get(url, params={'q':loc['q'], 'appid':key, 'units':'metric'}, timeout=5)
    if r.status_code==200:
        data = r.json()
        lst = data['list'][0]
        print('\n\n')
        print("Weather: ", lst['weather'][0]['description'])
        print('Temprature: ', lst['main']['temp'])
        print('Feels like: ', lst['main']['feels_like'])
        print('Humidity: ', lst['main']['humidity'])
        print('Wind Speed: ', lst['wind']['speed'])
        print('\n\n')
    else:
        print('Error:', r.json()['message'])

if __name__=='__main__':
    main()