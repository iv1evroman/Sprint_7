import pytest
from data import ORDER_DATA_1_COLOUR, ORDER_DATA_BOTH_COLOUR, ORDER_DATA_NO_COLOUR


class TestCreateOrder:
    @pytest.mark.parametrize(
        'order_data',
        [
            ORDER_DATA_1_COLOUR,
            ORDER_DATA_BOTH_COLOUR,
            ORDER_DATA_NO_COLOUR
        ]
    )
    def test_create_order(self, order_data, order_methods):
        status_code, response_context = order_methods.create_order(order_data)
        assert status_code == 201 and 'track' in response_context
