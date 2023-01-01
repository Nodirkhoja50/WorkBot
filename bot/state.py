import requests
BASE_URL = 'http://127.0.0.1:8000/api/'
def search_job():
    responce = requests.get(BASE_URL)
    print(responce)

search_job()