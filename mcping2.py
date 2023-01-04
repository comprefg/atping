import requests
server="185.107.194.138:33711"
url = "https://api.mcsrvstat.us/2/"+server
print(url)
resp = requests.get(url)
print(resp.status_code)
print(resp)
