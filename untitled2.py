import requests


url = input("enter vid link:\n")
r = requests.get(url, allow_redirects=True)

open('facebook.ico', 'wb').write(r.content)
