import allure


class TestGetOrders:
    @allure.title('Проверка на запрос получить список заказов в тело ответа возвращается список заказов.')
    def test_get_list_of_orders(self, order_methods):
        response = order_methods.get_list_of_orders()
        assert response[0] == 200 and 'orders' in response[1]
