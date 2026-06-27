#
import time
import requests

def check_api(api: str):
    time.sleep(2)
    try:
        response = requests.get(api, tiemeout=5)
        if response.status_code == 200:
            print(f'Success: {api} esta funcionando perfectamente')
        else:
            print(f'Error: {api} respondio con el código de estado {response.status_code}.')
    except requests.RequestException:
        print(f'Error: {api} esta caido.')
        

if __name__ == '__main__':
    start = time.time()
    
    apis = [
        "http://management.azure.com",
        "https://api.github.com",
        "https://api.openai.com",
        "https://outlook.office.com",
        "https://api.spotify.com",
        "http://graph.microsoft.com",
    ]
    
    for api in apis:
        check_api(api)
    
    end = time.time()
    
    print(f"Tiempo total de ejecución: {end - start:.4f} segundos")