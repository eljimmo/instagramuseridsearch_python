import requests

url = "https://instagram47.p.rapidapi.com/user_tagged_posts"

querystring = {"userid":"*****"}

headers = {
	"X-RapidAPI-Key": "************",
	"X-RapidAPI-Host": "instagram**.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)