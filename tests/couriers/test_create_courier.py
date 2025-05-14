import allure
import pytest
from methods.courier_methods import CourierMethods
from helpers import Helpers


class TestCreateCourier:

    @allure.title('Проверка кода ответа при успешном создании курьера')
    def test_create_courier_check_status_code_successful(self):
        courier_methods = CourierMethods()
        _, response = courier_methods.create_courier()
        assert response.status_code == 201

    @allure.title('Проверка текста ответа при успешном создании курьера')
    def test_create_courier_check_text_successful(self):
        courier_methods = CourierMethods()
        _, response = courier_methods.create_courier()
        assert response.text == '{"ok":true}'

    @allure.title('Проверка, что нельзя создать двух одинаковых курьеров')
    def test_create_courier_check_two_same_couriers_creation(self):
        courier_methods = CourierMethods()
        courier, _  = courier_methods.create_courier()
        _, response = courier_methods.create_courier(courier)
        assert response.status_code == 409 and \
               response.text == '{"code":409,"message":"Этот логин уже используется. Попробуйте другой."}'

    @allure.title('Проверка, что нельзя создать курьера с уже существующим логином')
    def test_create_courier_check_same_login_creation(self):
        courier_methods = CourierMethods()
        courier, _ = courier_methods.create_courier()
        courier_2 = {'login': courier['login'],
                     'password': courier['password'] + '1',
                     'firstName': courier['firstName'] + '1'}
        _, response = courier_methods.create_courier(courier_2)
        assert response.status_code == 409 and \
               response.text == '{"code":409,"message":"Этот логин уже используется. Попробуйте другой."}'


    @allure.title('Проверка, что нельзя создать курьера если нет одного из обязательных полей')
    @pytest.mark.parametrize("absent_field", ['login', 'password'])
    def test_create_courier_check_required_field_absence(self, absent_field):
        courier_methods = CourierMethods()
        courier = {'login': Helpers.generate_random_string(10),
                   'password': Helpers.generate_random_string(10),
                   'firstName': Helpers.generate_random_string(10)}
        del courier[absent_field]
        _, response = courier_methods.create_courier(courier)
        assert response.status_code == 400 and \
               response.text == '{"code":400,"message":"Недостаточно данных для создания учетной записи"}'
