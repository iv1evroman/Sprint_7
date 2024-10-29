import requests
import random
import string
from data import BASE_URL, COURIERS_URL, LOGIN_URL
import allure


class CourierMethods:
    @allure.step('создаем нового курьера')
    def create_new_courier(self, login, password, first_name):
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }
        response = requests.post(f'{BASE_URL}{COURIERS_URL}', data=payload)
        return response.status_code, response.json()

    @allure.step('метод регистрации нового курьера возвращает список из логина и пароля '
                 'если регистрация не удалась, возвращает пустой список')
    def register_new_courier_and_return_login_password(self):
        # метод генерирует строку, состоящую только из букв нижнего регистра, в качестве параметра передаём длину строки
        def generate_random_string(length):
            letters = string.ascii_lowercase
            random_string = ''.join(random.choice(letters) for i in range(length))
            return random_string

        # создаём список, чтобы метод мог его вернуть
        login_pass = []

        # генерируем логин, пароль и имя курьера
        login = generate_random_string(10)
        password = generate_random_string(10)
        first_name = generate_random_string(10)

        # собираем тело запроса
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

        # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)

        # если регистрация прошла успешно (код ответа 201), добавляем в список логин и пароль курьера
        if response.status_code == 201:
            login_pass.append(login)
            login_pass.append(password)
            login_pass.append(first_name)

        # возвращаем список
        return login_pass

    @allure.step('Авторизуем курьера')
    def login_courier(self, login, password):
        payload = {
        "login": login,
        "password": password
    }
        response = requests.post(f'{BASE_URL}{COURIERS_URL}{LOGIN_URL}', data=payload)
        return response.status_code, response.json()

    @allure.step('Удаляем курьера')
    def delete_courier(self, id):
        response = requests.delete(f'{BASE_URL}{COURIERS_URL}{id}')
        return response.status_code, response.json()
