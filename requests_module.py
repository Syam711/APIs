import requests

r = requests.get('https://jsonplaceholder.typicode.com/users')
data = r.json()
print(data)

