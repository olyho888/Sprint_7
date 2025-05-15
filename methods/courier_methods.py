import allure
import requests
from data import Data
from helpers import Helpers

class CourierMethods:

    @allure.step('Создание курьера')
    def create_courier(self, params=None):
        if params is None:
            params = {'login': Helpers.generate_random_string(10),
                      'password': Helpers.generate_random_string(10),
                      'firstName': Helpers.generate_random_string(10)}
        response = requests.post(url=f'{Data.COURIERS_URL}', data=params)
        return params, response

    @allure.step('Создание курьера с проверкой успешности')
    def create_courier_successful(self, params=None):
        if params is None:
            params = {'login': Helpers.generate_random_string(10),
                      'password': Helpers.generate_random_string(10),
                      'firstName': Helpers.generate_random_string(10)}
        response = requests.post(url=f'{Data.COURIERS_URL}', data=params)
        if response.status_code == 201:
            del params['firstName']
            return params
        else:
            raise AssertionError('Ошибка при создании курьера')

    @allure.step('Авторизация курьера')
    def login_courier(self, params):
        courier_id = None
        response = requests.post(url=f'{Data.COURIERS_URL}/login', data=params)
        if response.status_code == 200:
            courier_id = response.json()['id']
        return courier_id, response

    @allure.step('Авторизация курьера с проверкой успешности')
    def login_courier_successful(self, params):
        response = requests.post(url=f'{Data.COURIERS_URL}/login', data=params)
        if response.status_code == 200:
            courier_id = response.json()['id']
            return courier_id
        else:
            raise AssertionError('Ошибка при авторизации курьера')

    @allure.step('Удаление курьера')
    def delete_courier(self, courier_id):
        response = requests.delete(url=f'{Data.COURIERS_URL}/{courier_id}')
        return response
