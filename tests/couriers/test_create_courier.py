from data import COURIER_PASSWORD, COURIER_NAME
from helpers import Helpers


class TestCreateCourier:
    def test_create_courier(self, courier_methods):
        random_login = Helpers.create_random_login(self)
        response = courier_methods.create_new_courier(random_login, COURIER_PASSWORD, COURIER_NAME)
        assert response[0] == 201 and {'ok': True} == response[1]

    def test_create_same_courier_two_times(self, courier_methods):
        random_login = Helpers.create_random_login(self)
        courier_methods.create_new_courier(random_login, COURIER_PASSWORD, COURIER_NAME)
        result = courier_methods.create_new_courier(random_login, COURIER_PASSWORD, COURIER_NAME)
        assert (result[0] == 409 and
                {'code': 409, 'message': 'Этот логин уже используется. Попробуйте другой.'} == result[1])

    def test_create_courier_without_login(self, courier_methods):
        result = courier_methods.create_new_courier('', COURIER_PASSWORD, COURIER_NAME)
        assert (result[0] == 400 and
                {'code': 400, 'message': 'Недостаточно данных для создания учетной записи'} == result[1])
