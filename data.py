class Data:

    BASE_URL = 'https://qa-scooter.praktikum-services.ru/api/v1'
    ORDERS_URL = f'{BASE_URL}/orders'
    COURIERS_URL = f'{BASE_URL}/courier'

    ORDERS_DATA = [
        {
            "firstName": "Иван",
            "lastName": "Иванов",
            "address": "ул. Пушкина, д. 10",
            "metroStation": 1,
            "phone": "89991234567",
            "rentTime": 2,
            "deliveryDate": "2025-05-17",
            "comment": "Доставить к подъезду",
            "color": []
        },
        {
            "firstName": "Петр",
            "lastName": "Петров",
            "address": "пр. Ленина, д. 20",
            "metroStation": 2,
            "phone": "89007654321",
            "rentTime": 5,
            "deliveryDate": "2025-05-18",
            "comment": "Позвонить за час"
        }
    ]
