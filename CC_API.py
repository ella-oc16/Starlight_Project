import requests

class CC_API():
    def __init__(self, client_id, client_secret, redirect_uri, auth_code) -> None:
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri
        self.auth_code = auth_code
        self.token_headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        self.api_token_url = 'https://cashcalc.co.uk/oauth/token'
        self.access_token = None
        self.default_headers = {'Accept': 'application/json', 'Authorization': self.access_token, 'X-Client-ID': self.client_id[:-1]}
          
    # returns the access token (also adds refresh token to file)
    def accessToken_withAuthCode(self):
        print('----- GETTING ACCESS TOKEN USING OAUTH CODE -----------')
        parameters = f'grant_type=authorization_code&code={self.auth_code}&redirect_uri={self.redirect_uri}&client_id={self.client_id}&client_secret={self.client_secret}'
        response = requests.post(url=self.api_token_url, data=parameters, headers=self.token_headers)
        response = response.json()
            
        if 'error' in response:
            print(response)
            return False
            
        print('success')
    
        # add latest refresh token to file
        with open("RefreshToken.txt", mode='w') as f:
            f.write(response['refresh_token'])

        self.access_token = response['access_token']
        return response['access_token']

    # returns the access token (also adds refresh token to file)
    def accessToken(self):
        print('----- GETTING ACCESS TOKEN USING REFRESH TOKEN -----------')
        with open("RefreshToken.txt", mode='r') as f:
            lines = f.readlines()
            refresh_token = str(lines[0])
            
        parameters = f'grant_type=refresh_token&refresh_token={refresh_token}&client_id={self.client_id}&client_secret={self.client_secret}'
        response = requests.post(url=self.api_token_url, data=parameters, headers=self.token_headers)
        response = response.json()

        if 'error' in response:
            print(response)
            return False
            
        print('success')
            
        with open("RefreshToken.txt", mode='w') as f:
            f.write(response['refresh_token'])
            
        self.access_token = response['access_token']
        self.default_headers = {'Accept': 'application/json', 'Authorization': self.access_token, 'X-Client-ID': self.client_id[:-1]}
        return response['access_token']
    
    def get_clients(self):
        print('getting client info.....')
        advisor, per_page, page_number = 'Denis', 10, 1
        req = f'https://cashcalc.co.uk/api/v3.3/clients?search={advisor}&per_page={per_page}&page={page_number}'
        resp = requests.get(url=req, headers=self.default_headers)
        print(resp)
        resp = resp.json()
        print(resp)