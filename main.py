# Import libraries for graph and https
import matplotlib.pyplot as plt
import requests

# Get user's IP address
ip = requests.get('https://api.ipify.org').text

# Get location data from webAPI using IP address
response = requests.get(f'https://ipgeolocation.abstractapi.com/v1/?api_key=08497c09676b46d1aeb921bc0f5481fa&ip_address={ip}')

if response.status_code == 200:
  
  # Get longtiude and latitude from response
  location = response.json()
  longitude = location['longitude']
  latitude = location['latitude']
  
  # Use longitude and latitude to get rain data from webAPI
  response2 = requests.get(f'https://api.open-meteo.com/v1/forecast?latitude={str(latitude)}&longitude={str(longitude)}&hourly=rain')

  if response2.status_code == 200:
    
    data = response2.json()
    time = data['hourly']['time']
    precipitation = data['hourly']['rain']
    
    # Plot rain data
    plt.figure(figsize=(50, 10))
    plt.plot(time, precipitation, marker='o', linestyle='-')
    plt.title('Rain in ' + location['city'])
    plt.xlabel('Time ')
    plt.ylabel('Rain precipitation (mm)')
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.show()
    
  else:
    print("Error getting rain data")

else:
  print(f"Oh nooose something went wrong: {response.status_code} - {response.reason}")
