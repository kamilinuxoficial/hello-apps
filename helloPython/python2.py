import requests
r = requests.get("https://kamilinux.com/")
r.status_code
print(r.status_code)
print(r.encoding)
