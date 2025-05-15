import allure
import pytest
from methods.order_methods import OrderMethods


class TestOrdersList:

    @allure.title('Проверка списка заказов без курьера')
    @pytest.mark.parametrize("orders_params",[
        None,
        {'nearestStation': ["1", "2"]},
        {'limit': 10},
        {'page': 0},
        {'nearestStation': ["1", "2"], 'limit': 1, 'page': 1}
    ])
    def test_orders_list_without_courier(self, orders_create_fixture, orders_params):
        order_methods = OrderMethods()
        orders, response = order_methods.get_orders(orders_params)
        assert (response.status_code == 200) and (len(orders) > 0)

    @allure.title('Проверка списка заказов с указанием id курьера')
    @pytest.mark.parametrize("orders_params",[
        {},
        {'nearestStation': ["1", "2"]},
        {'limit': 10},
        {'page': 0},
        {'nearestStation': ["1", "2"], 'limit': 1, 'page': 1}
    ])
    def test_orders_list_with_courier_id(self, courier_create_login_fixture, orders_create_fixture, orders_params):
        orders_params['courierId'] = courier_create_login_fixture
        order_methods = OrderMethods()
        for order_id in orders_create_fixture:
            params = {'id': order_id, 'courierId': courier_create_login_fixture}
            order_methods.accept_order(params)
        orders, response = order_methods.get_orders(orders_params)
        assert (response.status_code == 200) and (len(orders) > 0)
