import allure
import pytest
from methods.courier_methods import CourierMethods


class TestLoginCourier:

    @allure.title('Проверка кода ответа при успешном логине курьера')
    def test_login_courier_check_status_code_successful(self, courier_create_fixture):
        courier_methods = CourierMethods()
        _, response = courier_methods.login_courier(courier_create_fixture)
        assert response.status_code == 200

    @allure.title('Проверка id при успешном логине курьера')
    def test_login_courier_check_id_successful(self, courier_create_fixture):
        courier_methods = CourierMethods()
        courier_id, response = courier_methods.login_courier(courier_create_fixture)
        assert ('{"id":' in response.text) and (courier_id is not None)

    @allure.title('Проверка, что нельзя залогиниться с некорректными/несуществующими данными')
    @pytest.mark.parametrize("incorrect_field", ['login', 'password'])
    def test_login_courier_check_incorrect_data(self, courier_create_fixture, incorrect_field):
        courier_methods = CourierMethods()
        courier = dict(courier_create_fixture)
        courier[incorrect_field] += '1'
        courier_id, response = courier_methods.login_courier(courier)
        assert response.status_code == 404 and \
               response.text == '{"code":404,"message":"Учетная запись не найдена"}'

    @allure.title('Проверка, что нельзя залогиниться если нет одного из обязательных полей')
    @pytest.mark.parametrize("absent_field, status_code, text", [
        ('login', 400, '{"code":400,"message":"Недостаточно данных для входа"}'),
        ('password', 504, 'Service unavailable')
    ])
    def test_login_courier_check_required_field_absent(self, courier_create_fixture, absent_field, status_code, text):
        courier_methods = CourierMethods()
        courier = dict(courier_create_fixture)
        del courier[absent_field]
        _, response = courier_methods.login_courier(courier)
        assert response.status_code == status_code and response.text == text
