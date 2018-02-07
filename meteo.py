#-*- coding:utf-8 -*-

# importer requests pour pouvoir travailler avec http.get
import requests
import json

while True:
    cite = raw_input("donnez le nom de votre ville? ")
    #recuperation de l'url
    response = requests.get(
    "http://api.openweathermap.org/data/2.5/weather?q="+cite+"&appid=f61f0971b4ff1021ef7fd6074c521ac6")
    #permet de convertir Json en dictionnaire de python
    data = json.loads(response.content)
    print ("la temperature actuel de cette ville est de : \n" + str(data['main']['temp'] - 273.15)+ "°") 
