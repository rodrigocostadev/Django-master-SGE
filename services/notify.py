import requests

class Notify:
    
    def __init__(self):
        # self.__base_url = '	https://webhook.site'
        self.__base_url = 'http://localhost:8001'
    
    def send_order_event(self, data):
        # reponse = requests.post(
        requests.post(
            # url=f'{self.__base_url}/7052529c-c8d5-46e7-8815-3cf60ee9bbf1',
            url=f'{self.__base_url}/api/v1/webhooks/order/',
            json=data,
        )
        # return reponse.json()