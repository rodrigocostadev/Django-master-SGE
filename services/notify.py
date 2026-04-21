import requests

class Notify:
    
    def __init__(self):
        self.__base_url = '	https://webhook.site'
    
    def send_event(self, data):
        # reponse = requests.post(
        requests.post(
            url=f'{self.__base_url}/7052529c-c8d5-46e7-8815-3cf60ee9bbf1',
            json=data,
        )
        # return reponse.json()