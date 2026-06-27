#
import time
import requests

def check_api(api: str):
    time.sleep(2)
    try:
        response = requests.get(api)
        if response.status_code == 200:
            print(f'Success: {api} esta funcionando perfectamente')
        else:
            print(f'Error: {api} respondio con el código de estado {response.status_code}.')
    except requests.RequestException:
        print(f'Error: {api} esta caido.')
        

