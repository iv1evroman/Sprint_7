from data import BASE_URL, ORDERS_URL
import requests
import json
import allure

class OrderMethods:
    @allure.step('создаем заказ и получаем код с телом ответа')
    def create_order(self, params):
        response = requests.post(f'{BASE_URL}{ORDERS_URL}', json.dumps(params))
        return response.status_code, response.json()

    @allure.step('отправляем запрос на получение списка заказов и получаем код с заказами в теле ответа')
    def get_list_of_orders(self):
        response = requests.get(f'{BASE_URL}{ORDERS_URL}')
        return response.status_code, response.json()

    @allure.step('отменяем заказ')
    def delete_order(self, track_id):
        payload = {
            "track": track_id
        }
        requests.put(f'{BASE_URL}{ORDERS_URL}cancel', json.dumps(payload))
