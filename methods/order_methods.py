from data import BASE_URL, ORDERS_URL
import requests
import json


class OrderMethods:
    def create_order(self, params):
        response = requests.post(f'{BASE_URL}{ORDERS_URL}', json.dumps(params))
        return response.status_code, response.json()
    def get_list_of_orders(self):
        response = requests.get(f'{BASE_URL}{ORDERS_URL}')
        return response.status_code, response.json()
