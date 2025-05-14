import pytest
from methods.courier_methods import CourierMethods
from data import Data
from methods.order_methods import OrderMethods


@pytest.fixture
def courier_create_fixture():
    courier_methods = CourierMethods()
    courier, response = courier_methods.create_courier()
    if response.status_code == 201:
        del courier['firstName']
        return courier
    else:
        raise AssertionError('Ошибка при создании курьера')

@pytest.fixture
def courier_create_login_fixture():
    courier_methods = CourierMethods()
    courier, response = courier_methods.create_courier()
    if response.status_code == 201:
        del courier['firstName']
        courier_id, response = courier_methods.login_courier(courier)
        if response.status_code == 200:
            yield courier_id
            courier_methods.delete_courier(courier_id)
        else:
            raise AssertionError('Ошибка при авторизации курьера')
    else:
        raise AssertionError('Ошибка при создании курьера')

@pytest.fixture
def orders_create_fixture():
    error, error_message = False,""
    orders = []
    order_methods = OrderMethods()
    for order_data in Data.ORDERS_DATA:
        track, response = order_methods.create_order(order_data)
        if response.status_code == 201:
            order_id, response = order_methods.get_order_id(track)
            if response.status_code == 200:
                orders.append(order_id)
            else:
                error = True
                error_message = "Ошибка при получении id заказа"
                break
        else:
            error = True
            error_message = "Ошибка при создании заказа"
            break
    if not error:
        yield orders
        for order_id in orders:
            order_methods.finish_order(order_id)
    else:
        raise AssertionError(error_message)
