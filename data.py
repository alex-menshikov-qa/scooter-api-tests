class Config:
    URL = "https://qa-scooter.praktikum-services.ru"


class OrderData:
    @staticmethod
    def get_order_data():
        return {
            "firstName": "Max",
            "lastName": "Payne",
            "address": "123 Main St",
            "metroStation": "Metro Station",
            "phone": "+7234567890",
            "rentTime": 5,
            "deliveryDate": "2024-09-30",
            "comment": "Please leave at the front door",
        }
