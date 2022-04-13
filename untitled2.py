import requests


url = input("enter vid link:\n")
r = requests.get(url, allow_redirects=True)

open('download.mp4', 'wb').write(r.content)
