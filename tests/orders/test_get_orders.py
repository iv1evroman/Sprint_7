class TestGetOrders:
    def test_get_list_of_orders(self, order_methods):
        response = order_methods.get_list_of_orders()
        assert 'orders' in response[1]


