import requests

def client():
    credentials = {
        'username': 'yasin',
        'password': '123'
    }

    response = requests.post(
        url = 'https://127.0.0.1:8000/api/rest-auth/login/',
        data = credentials
    )

    print('Status code', response.status_code)

    