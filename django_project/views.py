import requests
from django.shortcuts import render

def home(request):
  #USING APIS => Example 1
  response = requests.get('https://api.github.com/events')
  data = response.json()
  results = data[0]["repo"]

  # Example 2
  response2 = requests.get('https://dog.ceo/api/breeds/image/random')
  data2 = response2.json()
  result2 = data2["message"]

  return render(request, 'templates/index.html', {'results': results, 'result2': result2})

  