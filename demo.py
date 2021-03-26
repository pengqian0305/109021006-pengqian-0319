import requests 
req = requests.get("http://210.70.80.21/~bs109021006/")
print(req.status_code)