import requests
import json

def get_access_token(client_id, client_secret, scope):
    token_url = 'https://api.orange.com/oauth/v3/token'
    payload = {
        'grant_type': 'client_credentials',
        'client_id': client_id,
        'client_secret': client_secret,
        'scope': scope
    }

    response = requests.post(token_url, data=payload)
    response_data = response.json()
    access_token = response_data.get('access_token')

    return response_data['access_token']

def call_api(access_token):
    api_url = 'https://api.orange.com/camara/location-retrieval/orange-lab/v0/retrieve'
    headers = {
        'Authorization': f'Bearer {access_token}',
        'x-correlator': 'your_correlator'
    }
    data = {
        "device": {
            "phoneNumber": "phone_number_test"
        },
        "maxAge": 60
    }
    response = requests.post(api_url, headers=headers, json=data)
    return response.json()

# Replace 'your_client_id' and 'your_client_secret' with actual values
client_id = 'your_client_id'
client_secret = 'your_client_secret'
scope = ""

access_token = get_access_token(client_id, client_secret, scope)
api_response = call_api(access_token)
print(json.dumps(api_response, indent=4))
