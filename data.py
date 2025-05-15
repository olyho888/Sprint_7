class Data:

    BASE_URL = 'https://qa-scooter.praktikum-services.ru/api/v1'
    ORDERS_URL = f'{BASE_URL}/orders'
    COURIERS_URL = f'{BASE_URL}/courier'

    error_create_courier_400 = '{"code":400,"message":"Недостаточно данных для создания учетной записи"}'
    error_create_courier_409 = '{"code":409,"message":"Этот логин уже используется. Попробуйте другой."}'
    error_login_courier_400 = '{"code":400,"message":"Недостаточно данных для входа"}'
    error_login_courier_404 = '{"code":404,"message":"Учетная запись не найдена"}'
    error_504 = 'Service unavailable'

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
