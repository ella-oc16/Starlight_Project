import requests
import webbrowser

# to obtain the authorisation code, run this script and you should be talken to OAuth login
# login to cashcalc using company credentials 
# you will be redirected to a local web server
# authorisation code can be found in the url
# copy the 'code' part

f=open(r"C:\Users\oconn\OneDrive\Desktop\starlight_info.txt","r")
lines=f.readlines()
CLIENT_ID = str(lines[1])
REDIRECT_URI = str(lines[7])
f.close()

# scope of informarion want to access from api
SCOPE = 'client-finances client-info'

cashcalc_url = f'https://cashcalc.co.uk/oauth/authorize?response_type=code&client_id={CLIENT_ID}&redirect_uri={REDIRECT_URI}&scope={SCOPE}'

response = requests.get(url=cashcalc_url)
webbrowser.open(cashcalc_url)





