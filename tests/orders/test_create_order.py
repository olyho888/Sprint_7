import allure
import pytest
from data import Data
from methods.order_methods import OrderMethods

class TestCreateOrder:

    @allure.title('Проверка, что возможно создать заказ с разными цветами самоката')
    @pytest.mark.parametrize("color", [['GREY'], ['BLACK'], ['GREY', 'BLACK'], []])
    def test_create_order_with_different_colors(self, color):
        order_methods = OrderMethods()
        order_data = Data.ORDERS_DATA[0]
        order_data["color"] = color
        _, response = order_methods.create_order(order_data)
        assert (response.status_code == 201) and ('{"track":' in response.text)

    @allure.title('Проверка, что возможно создать заказ без передачи цвета самоката')
    def test_create_order_without_color(self):
        order_methods = OrderMethods()
        _, response = order_methods.create_order(Data.ORDERS_DATA[1])
        assert (response.status_code == 201) and ('{"track":' in response.text)

    @allure.title('Проверка, что возвращается track при успешном создании заказа')
    @pytest.mark.parametrize("order_data", Data.ORDERS_DATA)
    def test_create_order_check_track_successful_(self, order_data):
        order_methods = OrderMethods()
        track, response = order_methods.create_order(order_data)
        assert (response.status_code == 201) and ('{"track":' in response.text)
