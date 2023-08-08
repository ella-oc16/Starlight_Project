import requests
import json

# read this info in from a file, below should all be strings
REDIRECT_URI = 'https//localhost/'
CLIENT_ID = 'cbbcuwum'
SCOPE = 'client-finances client-info'

cashcalc_url = f'https://cashcalc.co.uk/oauth/authorize?response_type=code&client_id={CLIENT_ID}&redirect_uri={REDIRECT_URI}&scope={SCOPE}'

#response = requests.get(url=cashcalc_url)
#print(response.headers)

autho_code = 'gdhdujd'

# Authorization : Bearer {access_token} (Required) The obtained token must be added as a Bearer token as a header, it should be a string
ACCEPT_TYPE = 'application/json'
default_headers = {'Accept': ACCEPT_TYPE, 'Authorization': autho_code, 'X-Client-ID': CLIENT_ID}

#request a list of all clients
advisor = 'denis'
per_page = 10
page_number = 2
#clients_request = f'https://cashcalc.co.uk/api/v3.3/clients?search={advisor}&per_page={per_page}&page={page_number}'
#clients_response = requests.get(url=clients_request, headers=default_headers)
#list_of_clients = clients_response.json()

#check if 

#get response into dictionary form, as seen below
example_client_response = {
    "status": "success",
    "data": {
        "clients": [
            {
                "id": 1,
                "name": "Kieran Moore & Julie Moore",
                "clients": [
                    {
                        "uuid": "b63d27a0-5ba1-11e9-8d25-5171fc0a1b2f",
                        "name": "Kieran Moore",
                        "dob": "1956-12-24T00:00:00Z",
                        "gender": "male"
                    },
                    {
                        "uuid": "f1d2c660-5ba2-11e9-932f-e98a8b3f91f7",
                        "name": "Julie Moore",
                        "dob": "1959-01-10T00:00:00Z",
                        "gender": "female"
                    }
                ],
                "adviser": {
                    "uuid": "d225dfa0-5ba0-11e9-96e7-df430c1626cf",
                    "name": "Example Adviser"
                },
                "links": {
                    "self": "https://cashcalc.co.uk/api/v3.3/clients/1",
                    "incomes": "https://cashcalc.co.uk/api/v3.3/clients/1/incomes",
                    "expenses": "https://cashcalc.co.uk/api/v3.3/clients/1/expenses",
                    "investments": "https://cashcalc.co.uk/api/v3.3/clients/1/investments",
                    "pensions": "https://cashcalc.co.uk/api/v3.3/clients/1/pensions",
                    "assets": "https://cashcalc.co.uk/api/v3.3/clients/1/assets",
                    "liabilities": "https://cashcalc.co.uk/api/v3.3/clients/1/liabilities",
                    "notes": "https://cashcalc.co.uk/api/v3.3/clients/1/notes",
                    "contacts": "https://cashcalc.co.uk/api/v3.3/clients/1/contacts",
                    "addresses": "https://cashcalc.co.uk/api/v3.3/clients/1/addresses"
                },
            },
        ]
    },
    "links": {
        "first": "https://cashcalc.co.uk/api/v3.3/clients?page=1",
        "last": "https://cashcalc.co.uk/api/v3.3/clients?page=2",
        "next": "https://cashcalc.co.uk/api/v3.3/clients?page=2"
    },
    "meta": {
        "current_page": 1,
        "from": 1,
        "last_page": 2,
        "path": "https://cashcalc.co.uk/api/v3.3/clients",
        "per_page": 10,
        "to": 10,
        "total": 18
    }
}

if example_client_response["status"] != 'success':
    print('ERROR')


list_of_clients = example_client_response["data"]["clients"]
print(list_of_clients[0]['name'])


for client in list_of_clients:
    client_id = client['id']
    sub_clients = client['clients']
    for sub in sub_clients:
        user_id = sub['uuid']
        name = sub['name']
        dob = sub['dob']
        print(f'user id = {user_id}, name = {name}, date of birth = {dob}')


# go through all clients and check if they are in database
# if not in database, then add them to databasae
# append the below information 


data_types = ['personals', 'employments', 'addresses', 'contacts', 'relations']

def get_info(client_id: int, data_type = 'employments', headers = default_headers):
    request = f'https://cashcalc.co.uk/api/v3.3/clients/{client_id}/{data_type}'
    response = requests.get(url=request, headers=headers)
    response = response.json()

    if response["status"] != 'success':
        print('ERROR')
        return
    
    #might have to edit data_type (for example, employments has employment here)
    data = response['data'][data_type][0]       # gives a dict of all info
    return data

personal_data = get_info(client_id=1, data_type=data_types[0])

