import requests
import json

base_url = 'http://127.0.0.1:8000/api/'

login_url = base_url + 'auth/token/'

products_url = base_url + 'products/'

refresh_url = login_url + 'refresh/'

# requests.post(login_url, data=None, headers=None, params=None)

# Auth test
data = {
	'username': 'testuser',
	'password': 'test1234',
}
login_r = requests.post(login_url, data=data)

json_data = login_r.json() #login_r.text

print(json.dumps(json_data, indent=2))

token = json_data['token']

# Retrive products test

headers = {
	'Authorization': 'JWT %s' % (token)
}
p_r = requests.get(products_url, headers=headers)

prod_json_data = p_r.json()
print (json.dumps(prod_json_data, indent=2))

# Refresh URL token

data = {
	'token': token
}
refresh_r = requests.post(refresh_url, data=data)

print(refresh_r.json())

token = refresh_r.json()['token']