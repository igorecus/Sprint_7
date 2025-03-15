
class Data:
    DUPLICATE_LOGIN = "Этот логин уже используется. Попробуйте другой."
    MISSING_FIELDS = "Недостаточно данных для создания учетной записи"
    LOGIN_DATA_MISSING = "Недостаточно данных для входа"
    USER_NOT_FOUND = "Учетная запись не найдена"

order_base = {
    "firstName": "Naruto",
    "lastName": "Uchiha",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2025-03-16",
    "comment": "Saske, come back to Konoha"
}

order_black = {**order_base, "color": ["BLACK"]}
order_gray = {**order_base, "color": ["GREY"]}
order_both = {**order_base, "color": ["BLACK", "GREY"]}
order_no_color = {**order_base}