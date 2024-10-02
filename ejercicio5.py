import sys
import requests

def check_status(url,num):
    
    for i in range(0,num):
        
        try:
            respuesta = requests.get(url,timeout=5)
            print(respuesta.status_code, url)
        except requests.exceptions.RequestException as error:
            print("Error: "+error)
    

input=sys.argv[1]

if(input.startswith('https://')):
    check_status(input,1)
else:
    url='https://'+input
    check_status(url,1)