import allure
import json
import requests
from data import Data


class OrderMethods:

    @allure.step('Создание заказа')
    def create_order(self, params):
        track = None
        response = requests.post(url=f'{Data.ORDERS_URL}', json=params)
        if response.status_code == 201:
            track = response.json()['track']
        return track, response

    @allure.step('Принятие заказа')
    def accept_order(self, params):
        response = requests.put(url=f'{Data.ORDERS_URL}/accept/{params['id']}?courierId={params['courierId']}')
        return response

    @allure.step('Завершение заказа')
    def finish_order(self, order_id):
        response = requests.put(url=f'{Data.ORDERS_URL}/finish/{order_id}')
        return response

    @allure.step('Получение id заказа по его номеру')
    def get_order_id(self, track):
        order_id = None
        response = requests.get(url=f'{Data.ORDERS_URL}/track?t={track}')
        if response.status_code == 200:
            order_id = response.json()['order']['id']
        return order_id, response

    @allure.step('Получение списка заказов')
    def get_orders(self, params=None):
        orders = []
        url_params = ""
        if params is not None:
            for key, value in params.items():
                url_params += "&" if len(url_params) > 0 else ""
                url_params += f"{key}={json.dumps(value)}"
            url_params = "?" + url_params
        response = requests.get(url=f"{Data.ORDERS_URL}{url_params}")
        if response.status_code == 200:
            orders = response.json()['orders']
        return orders, response
