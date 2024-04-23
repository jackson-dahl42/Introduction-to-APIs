import matplotlib.pyplot as plt
import requests

ip = input("enter ip address:")
response = requests.get('https://ipgeolocation.abstractapi.com/v1/?api_key=08497c09676b46d1aeb921bc0f5481fa&ip_address=' + ip)

location = response.json()
longitude = location['longitude']
latitude = location['latitude']

response2 = requests.get('https://api.open-meteo.com/v1/forecast?latitude=' + str(latitude) + '&longitude=' + str(longitude) + '&hourly=rain')
data = response2.json()
time = data['hourly']['time']
precipitation = data['hourly']['rain']

plt.figure(figsize=(50, 10))
plt.plot(time, precipitation, marker='o', linestyle='-')
plt.title('Rain in ' + location['city'])
plt.xlabel('Time ')
plt.ylabel('Rain precipitation (mm)')
plt.grid(True)
plt.xticks(rotation=45)
plt.show()