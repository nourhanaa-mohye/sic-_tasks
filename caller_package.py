import requests

data = {'Name': 'Nourhan', 'Age': '22'}
response = requests.post('http://localhost:3000/api/data', json=data)

print(response.status_code) 
