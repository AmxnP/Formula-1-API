# imports
import requests
import pandas as pd

api = 'https://api.openf1.org/v1/drivers'

response = requests.get(api)

if response.status_code == 200:
  data = response.json()
  print(data)
  df = pd.DataFrame(data)
  df.to_csv('drivers.csv')
else:
  print(f'Error:', response.status_code)
  
