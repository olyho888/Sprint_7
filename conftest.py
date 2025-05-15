import pytest
from methods.courier_methods import CourierMethods
from data import Data
from methods.order_methods import OrderMethods


@pytest.fixture
def courier_create_fixture():
    courier_methods = CourierMethods()
    courier = courier_methods.create_courier_successful()
    return courier

@pytest.fixture
def courier_create_login_fixture():
    courier_methods = CourierMethods()
    courier = courier_methods.create_courier_successful()
    courier_id = courier_methods.login_courier_successful(courier)
    yield courier_id
    courier_methods.delete_courier(courier_id)

@pytest.fixture
def orders_create_fixture():
    orders = []
    order_methods = OrderMethods()
    for order_data in Data.ORDERS_DATA:
        track = order_methods.create_order_successful(order_data)
        order_id = order_methods.get_order_id_successful(track)
        orders.append(order_id)
    yield orders
    for order_id in orders:
        order_methods.finish_order(order_id)
