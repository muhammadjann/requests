import httpx
from pprint import pprint
url = 'https://jsonplaceholder.typicode.com/users'
data = httpx.get(url=url)
data = data.json()
for i in data:
    with open(f"{i['username']}.txt",'w') as fhand:
        fhand.write(f" Name: {i['name']}")
        fhand.write(f" Username:{i['username']}")
        fhand.write(f" phone_number: {i['phone']}")
