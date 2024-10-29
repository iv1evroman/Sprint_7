import pytest
from methods.order_methods import OrderMethods
from methods.couriers_methods import CourierMethods


@pytest.fixture()
def order_methods():
    return OrderMethods()


@pytest.fixture()
def courier_methods():
    return CourierMethods()


@pytest.fixture()
def courier(courier_methods):
    login_pass = courier_methods.register_new_courier_and_return_login_password()
    response = courier_methods.login_courier(login_pass[0], login_pass[1])
    yield response.json()['id']
    courier_methods.delete_courier(response.json()['id'])
