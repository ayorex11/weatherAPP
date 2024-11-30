
import os 
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
import requests
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET'])
@permission_classes([AllowAny])
def get_current_weather(request, zip_code, country_code):
	API_key = os.getenv('API_KEY')
	url1 = f'http://api.openweathermap.org/geo/1.0/zip?zip={zip_code},{country_code}&appid={API_key}'
	response1 = requests.get(url1)

	lat_lon_data = response1.json()
	if response1.status_code != 200:
		return Response({'message':'Error Fetching Information based on input'}, status=response1.status_code)
	if 'lat' in lat_lon_data and 'lon' in lat_lon_data:
		latitude = lat_lon_data["lat"]
		longitude  = lat_lon_data["lon"]
		city = lat_lon_data["name"]

		url2 = f'https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={API_key}'
		response2 = requests.get(url2)

		weather = response2.json()

		if response2.status_code != 200:
			return Response({'message':'Error Fetching Weather Information. Try again later'}, status=response1.status_code)

		data ={'city':city,
			'temperature': weather['main']['temp'],
			'description': weather['weather'][0]['description'],
			}



		return Response(data, status=status.HTTP_200_OK)

	else:
		return Response({'error': 'Latitude and longitude not found in response'}, status=status.HTTP_404_NOT_FOUND)





