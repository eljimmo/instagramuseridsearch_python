import http.client

conn = http.client.HTTPSConnection("instagram**.p.rapidapi.com")

headers = {
    'X-RapidAPI-Key': "******************",
    'X-RapidAPI-Host': "instagram**.p.rapidapi.com"
    }

conn.request("GET", "/get_user_id?username=*******", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))