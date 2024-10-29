class TestLoginCourier:
    def test_login_courier(self, courier_methods):
        log_pass = courier_methods.register_new_courier_and_return_login_password()
        result = courier_methods.login_courier(log_pass[0], log_pass[1])
        assert result[0] == 200 and 'id' in result[1]

    def test_login_without_password(self, courier_methods):
        log_pass = courier_methods.register_new_courier_and_return_login_password()
        result = courier_methods.login_courier(log_pass[0], '')
        assert result[0] == 400 and {'code': 400, 'message': 'Недостаточно данных для входа'} == result[1]

    def test_login_without_login(self, courier_methods):
        log_pass = courier_methods.register_new_courier_and_return_login_password()
        result = courier_methods.login_courier('', log_pass[1])
        assert result[0] == 400 and {'code': 400, 'message': 'Недостаточно данных для входа'} == result[1]

    def test_login_with_incorrect_password(self, courier_methods):
        log_pass = courier_methods.register_new_courier_and_return_login_password()
        result = courier_methods.login_courier(log_pass[0], '12345')
        assert result[0] == 404 and {'code': 404, 'message': 'Учетная запись не найдена'} == result[1]

    def test_login_with_incorrect_login(self, courier_methods):
        log_pass = courier_methods.register_new_courier_and_return_login_password()
        result = courier_methods.login_courier('ivan', log_pass[1])
        assert result[0] == 404 and {'code': 404, 'message': 'Учетная запись не найдена'} == result[1]

