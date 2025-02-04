import requests
from selenium.webdriver.support.expected_conditions import title_is

import data

#Obtener todos los productos
def get_all_products():
    response = requests.get(data.url + data.get_products)
    response_status_code = response.status_code
    assert response_status_code == 200, "El status para obtener un producto NO es 200"
    return response.json()

#Obtener un producto por medio de la clave id
def get_a_product_by_id(id):
    response = requests.get(data.url + data.get_products + id)
    response_status_code = response.status_code
    assert type(id) == str
    assert response_status_code == 200, "El status para obtener un producto por medio del id NO es 200"
    return response.json()

#Obtener el valor de una clave del producto
def get_info_by_product():
    response = requests.get(data.url + data.get_products)
    response_status_code = response.status_code
    response_body = response.json()
    price_tshirt = response_body[0]["price"]
    title_shirt = response_body[0]["title"]
    assert response_status_code == 200, "El status para obtener el precio de un producto NO es 200"
    return price_tshirt, title_shirt
