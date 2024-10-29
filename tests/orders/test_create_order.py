import pytest
from data import ORDER_DATA_1_COLOUR, ORDER_DATA_BOTH_COLOUR, ORDER_DATA_NO_COLOUR
import allure


class TestCreateOrder:
    @pytest.mark.parametrize(
        'order_data',
        [
            ORDER_DATA_1_COLOUR,
            ORDER_DATA_BOTH_COLOUR,
            ORDER_DATA_NO_COLOUR
        ]
    )
    @allure.title('Проверка на успешное создание заказа с тремя разними вариантами выбора цвета'
                  ' и что тело ответа содержит track.')
    def test_create_order(self, order_data, order_methods):
        status_code, response_context = order_methods.create_order(order_data)
        assert status_code == 201 and 'track' in response_context
        order_methods.delete_order(response_context['track'])
